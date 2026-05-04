from ortools.sat.python import cp_model
from src.domain.rules import tecnico_liberado_para_cliente


class Solver:

    def __init__(self):
        self.alocacoes_cliente_dia = {}

    def alocar_chamado(self, chamado, agendas, tecnicos, lib_df):

        model = cp_model.CpModel()
        tempo = int(chamado['tempo_necessario'])

        possibilidades = []
        mapa = {}
        slots_map = {}

        for t in tecnicos:

            if not tecnico_liberado_para_cliente(t, chamado['cliente'], lib_df):
                continue

            if t not in agendas:
                continue

            agenda = agendas[t]
            datas = sorted(agenda['data'].dt.normalize().dropna().unique())

            for d in datas:

                if (chamado['cliente'], d.date()) in self.alocacoes_cliente_dia:
                    continue

                slots = agenda[
                    (agenda['data'].dt.normalize() == d) &
                    (agenda['agenda_efetivada'] == 'nao') &
                    (agenda['id'] == '')
                ]

                if len(slots) >= tempo:
                    var = model.NewBoolVar(f"{t}_{d}")
                    possibilidades.append((var, d.timestamp()))
                    mapa[(t, d)] = var
                    slots_map[(t, d)] = len(slots) - tempo

        if not possibilidades:
            return None, None, None

        model.AddExactlyOne(v for v, _ in possibilidades)
        model.Minimize(sum(ts * v for v, ts in possibilidades))

        solver = cp_model.CpSolver()
        status = solver.Solve(model)

        if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
            for (t, d), v in mapa.items():
                if solver.BooleanValue(v):
                    self.alocacoes_cliente_dia[(chamado['cliente'], d.date())] = t
                    return t, d, slots_map[(t, d)]

        return None, None, None
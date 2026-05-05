from src.data.loaders import (
    load_chamados,
    load_liberacao,
    get_tecnicos,
    load_agendas
)

from src.data.writers import (
    update_chamados,
    save_agendas,
    backup_chamados
)

from src.solver.solver import Solver

from src.domain.agenda import (
    build_schedule_dataframe,
    apply_schedule_to_agenda
)


def run():

    print("Iniciando pipeline...")

    backup_chamados()

    solver = Solver()

    while True:

        chamados_df = load_chamados()
        lib_df = load_liberacao()

        print("\nChamados restantes:", len(chamados_df))

        if chamados_df.empty:
            break

        tecnicos = get_tecnicos(lib_df)
        agendas = load_agendas(tecnicos)

        chamado = chamados_df.iloc[0]

        tecnico, data, slots = solver.alocar_chamado(
            chamado,
            agendas,
            tecnicos,
            lib_df
        )

        print("Resultado:", tecnico, data, slots)

        if not tecnico:
            chamados_df = chamados_df.iloc[1:]
            update_chamados(chamados_df)
            continue

        print(f"Alocado {chamado['id']} -> {tecnico} em {data}")

        df_alocacoes = build_schedule_dataframe(
            tecnico,
            data,
            [chamado],
            adicionar_deslocamento=False,
            slots_totais=slots
        )

        apply_schedule_to_agenda(tecnico, data, df_alocacoes, agendas)
        save_agendas(agendas)

        chamados_df = chamados_df.iloc[1:]
        update_chamados(chamados_df)

    print("Pipeline finalizado.")
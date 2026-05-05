import pandas as pd
from datetime import datetime
from pathlib import Path

# ==============================
# Caminhos do projeto (CORRIGIDO)
# ==============================

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

arquivo_tecnicos = DATA_DIR / "tecnicos.xlsx"
path_saida = DATA_DIR / "agenda.xlsx"

# ==============================
# Função de criação de agenda
# ==============================

def criar_agenda_tecnicos(
    arquivo_tecnicos=arquivo_tecnicos,
    data_inicio='2026-01-01',
    data_fim='2026-12-31',
    path_saida=path_saida
):
    df_tecnicos = pd.read_excel(arquivo_tecnicos)
    tecnicos = df_tecnicos['tecnicos'].tolist()

    inicio = pd.to_datetime(data_inicio)
    fim = pd.to_datetime(data_fim)
    dias = pd.date_range(start=inicio, end=fim)

    horarios = [
        "08:00", "09:00", "10:00", "11:00",
        "13:00", "14:00", "15:00", "16:00", "17:00"
    ]

    colunas = [
        'dia_da_semana', 'data', 'horario', 'status_agenda', 'agenda_efetivada',
        'id', 'cliente', 'maquina', 'tipo_manutencao',
        'tempo_necessario', 'prioridade', 'data_abertura'
    ]

    agendas_tecnicos = {}

    with pd.ExcelWriter(path_saida, engine='openpyxl') as writer:
        for tecnico in tecnicos:
            registros = []

            for dia in dias:
                dia_str = dia.strftime('%Y-%m-%d')
                semana = dia.strftime('%A')

                status = 'bloqueada' if semana in ['Saturday', 'Sunday'] else 'liberada'

                for hora in horarios:
                    registros.append({
                        'dia_da_semana': semana,
                        'data': dia_str,
                        'horario': hora,
                        'status_agenda': status,
                        'agenda_efetivada': '',
                        'id': '',
                        'cliente': '',
                        'maquina': '',
                        'tipo_manutencao': '',
                        'tempo_necessario': '',
                        'prioridade': '',
                        'data_abertura': ''
                    })

            df_agenda = pd.DataFrame(registros, columns=colunas)
            df_agenda.to_excel(writer, sheet_name=tecnico, index=False)

            agendas_tecnicos[tecnico] = df_agenda

    print(f"Arquivo '{path_saida}' criado com sucesso.")
    return agendas_tecnicos


# ==============================
# Execução (apenas uma vez)
# ==============================

agendas = criar_agenda_tecnicos(
    arquivo_tecnicos=arquivo_tecnicos,
    data_inicio='2026-01-01',
    data_fim='2026-12-31'
)

for tecnico, agenda in agendas.items():
    print(f"\nAgenda de {tecnico}")
    print(agenda)

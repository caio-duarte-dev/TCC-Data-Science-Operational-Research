import pandas as pd
from pathlib import Path

# ==============================
# Caminhos do projeto
# ==============================

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

path_chamados = DATA_DIR / "chamados.xlsx"

# ==============================
# Ordenação dos chamados
# ==============================

def ordenar_chamados(path_excel=path_chamados):
    try:
        chamados = pd.read_excel(path_excel)

        chamados['data_abertura'] = pd.to_datetime(chamados['data_abertura'])

        chamados_ordenados = chamados.sort_values(
            by=['prioridade', 'data_abertura', 'cliente'],
            ascending=[True, True, True]
        ).reset_index(drop=True)

        chamados_ordenados.to_excel(path_excel, index=False)

        return chamados_ordenados

    except FileNotFoundError:
        print(f"O arquivo {path_excel} não foi encontrado.")
        return pd.DataFrame()

# ==============================
# Execução
# ==============================

chamados_ordenados = ordenar_chamados()

print(chamados_ordenados)


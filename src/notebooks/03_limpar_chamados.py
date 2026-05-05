import pandas as pd
from pathlib import Path

# ==============================
# Caminhos do projeto
# ==============================

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

path_principal = DATA_DIR / "chamados.xlsx"
path_nao_agendados = DATA_DIR / "chamados_nao_agendados.xlsx"

# ==============================
# Limpeza dos chamados
# ==============================

def limpar_chamados(path_principal=path_principal, path_nao_agendados=path_nao_agendados):
    for path in [path_principal, path_nao_agendados]:
        try:
            df = pd.read_excel(path, nrows=0)

            df.to_excel(path, index=False)

            print(f"Todos os chamados foram apagados de '{path}', mantendo apenas o cabeçalho.")

        except FileNotFoundError:
            print(f"O arquivo '{path}' não foi encontrado.")

# ==============================
# Execução
# ==============================

limpar_chamados()


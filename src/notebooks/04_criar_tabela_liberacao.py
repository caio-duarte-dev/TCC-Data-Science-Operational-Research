import pandas as pd
import random
from pathlib import Path

# ==============================
# Caminhos do projeto
# ==============================

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

arquivo_clientes = DATA_DIR / "dados.xlsx"
arquivo_tecnicos = DATA_DIR / "tecnicos.xlsx"
path_saida = DATA_DIR / "liberacao_tecnicos_clientes.xlsx"

# ==============================
# Geração de liberação
# ==============================

def gerar_liberacao_tecnicos_clientes(
    arquivo_clientes=arquivo_clientes,
    arquivo_tecnicos=arquivo_tecnicos,
    path_saida=path_saida
):
    print("Iniciando leitura dos arquivos...")

    df_clientes = pd.read_excel(arquivo_clientes, sheet_name='clientes')
    print(f"Clientes carregados: {len(df_clientes)} linhas")

    df_tecnicos = pd.read_excel(arquivo_tecnicos)
    print(f"Técnicos carregados: {len(df_tecnicos)} linhas")

    clientes = df_clientes['clientes'].tolist()
    tecnicos = df_tecnicos['tecnicos'].tolist()

    print(f"Total de clientes: {len(clientes)}")
    print(f"Total de técnicos: {len(tecnicos)}")

    liberacoes = []

    print("Iniciando geração de combinações...")

    for i, cliente in enumerate(clientes):
        if i % 10 == 0:
            print(f"Processando cliente {i+1}/{len(clientes)}")

        entrada = {'cliente': cliente}

        for tecnico in tecnicos:
            entrada[tecnico] = random.choice(['liberado', 'bloqueado'])

        liberacoes.append(entrada)

    print("Criando DataFrame...")

    liberacao_df = pd.DataFrame(liberacoes)

    print("Salvando arquivo Excel...")

    liberacao_df.to_excel(path_saida, index=False)

    print(f"Arquivo '{path_saida}' criado com sucesso.")

    return liberacao_df


# ==============================
# Execução
# ==============================

print("Executando função principal...")
df_liberacao = gerar_liberacao_tecnicos_clientes()
print("Processo finalizado.")

print(df_liberacao)
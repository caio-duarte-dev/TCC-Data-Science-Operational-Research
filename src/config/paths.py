from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

CHAMADOS_PATH = DATA_DIR / "chamados.xlsx"
LIBERACAO_PATH = DATA_DIR / "liberacao_tecnicos_clientes.xlsx"
AGENDA_PATH = DATA_DIR / "agenda.xlsx"
VERIFICACAO_PATH = DATA_DIR / "chamados_verificacao.xlsx"
NAO_AGENDADOS_PATH = DATA_DIR / "chamados_nao_agendados.xlsx"
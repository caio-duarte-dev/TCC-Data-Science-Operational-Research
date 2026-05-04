import pandas as pd
import shutil
from src.config.paths import *


def update_chamados(df):
    df.reset_index(drop=True, inplace=True)
    df.to_excel(CHAMADOS_PATH, index=False)


def save_agendas(agendas):
    with pd.ExcelWriter(AGENDA_PATH, engine='openpyxl', mode='w') as writer:
        for t, df in agendas.items():
            df.to_excel(writer, sheet_name=t, index=False)


def backup_chamados():
    if CHAMADOS_PATH.exists():
        shutil.copyfile(CHAMADOS_PATH, VERIFICACAO_PATH)
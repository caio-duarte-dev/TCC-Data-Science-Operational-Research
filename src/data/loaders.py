import pandas as pd
from src.config.paths import *
from src.utils.normalization import normalize_text


def load_chamados():
    return pd.read_excel(CHAMADOS_PATH)


def load_liberacao():
    return pd.read_excel(LIBERACAO_PATH)


def get_tecnicos(lib_df):
    return list(lib_df.columns.drop('cliente'))


def load_agendas(tecnicos):
    xls = pd.ExcelFile(AGENDA_PATH)
    agendas = {}

    for t in tecnicos:
        if t in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=t)

            df['data'] = pd.to_datetime(df['data'], errors='coerce')

            df['agenda_efetivada'] = df['agenda_efetivada'].apply(normalize_text)
            df['status_agenda'] = df['status_agenda'].apply(normalize_text)

            df['id'] = df['id'].fillna('').astype(str).str.strip()

            agendas[t] = df

    return agendas
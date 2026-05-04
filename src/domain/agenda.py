import pandas as pd


# ==============================
# TIPAGEM PADRÃO DA AGENDA
# ==============================

def enforce_agenda_schema(df: pd.DataFrame) -> pd.DataFrame:

    TEXT_COLUMNS = [
        'id',
        'cliente',
        'maquina',
        'tipo_manutencao',
        'prioridade',
        'agenda_efetivada',
        'status_agenda'
    ]

    for col in TEXT_COLUMNS:
        if col in df.columns:
            df[col] = df[col].fillna("").astype(str)

    # 🔧 tratamento correto para datas
    if 'data_abertura' in df.columns:
        df['data_abertura'] = pd.to_datetime(df['data_abertura'], errors='coerce')

    return df


# ==============================
# BUILD SCHEDULE
# ==============================

def build_schedule_dataframe(
    tecnico,
    data,
    chamados,
    adicionar_deslocamento=False,
    slots_totais=None
):

    linhas = []
    total = 0

    for c in chamados:
        tempo = int(c['tempo_necessario'])
        total += tempo

        for _ in range(tempo):
            linhas.append({
                'tecnico': tecnico,
                'data': data,
                'id': c['id'],
                'cliente': c['cliente'],
                'maquina': c.get('maquina', ''),
                'tipo_manutencao': c.get('tipo_manutencao', ''),
                'tempo_necessario': tempo,
                'prioridade': c.get('prioridade', ''),
                'data_abertura': c.get('data_abertura', ''),
                'agenda_efetivada': 'sugerida',
                'status_agenda': 'liberada'
            })

    if adicionar_deslocamento and slots_totais is not None:
        if slots_totais - total >= 1:
            linhas.append({
                'tecnico': tecnico,
                'data': data,
                'id': 0,
                'cliente': 'deslocamento',
                'maquina': '',
                'tipo_manutencao': '',
                'tempo_necessario': 1,
                'prioridade': '',
                'data_abertura': '',
                'agenda_efetivada': 'sugerida',
                'status_agenda': 'liberada'
            })

    return pd.DataFrame(linhas)


# ==============================
# APPLY SCHEDULE
# ==============================

def apply_schedule_to_agenda(tecnico, data, df_alocacoes, agendas):

    agenda = agendas[tecnico]

    # 🔧 CORREÇÃO ESTRUTURAL AQUI
    agenda = enforce_agenda_schema(agenda)

    if isinstance(data, pd.Timestamp):
        data = data.date()

    mask = (
        (agenda['data'].dt.date == data) &
        (agenda['status_agenda'] == 'liberada') &
        (agenda['agenda_efetivada'] == 'nao') &
        (agenda['id'] == '')
    )

    slots = agenda.loc[mask]

    if len(slots) < len(df_alocacoes):
        return False

    for i, idx in enumerate(slots.index[:len(df_alocacoes)]):
        linha = df_alocacoes.iloc[i]

        agenda.at[idx, 'id'] = linha['id']
        agenda.at[idx, 'cliente'] = linha['cliente']
        agenda.at[idx, 'maquina'] = linha['maquina']
        agenda.at[idx, 'tipo_manutencao'] = linha['tipo_manutencao']
        agenda.at[idx, 'tempo_necessario'] = linha['tempo_necessario']
        agenda.at[idx, 'prioridade'] = linha['prioridade']
        agenda.at[idx, 'data_abertura'] = linha['data_abertura']
        agenda.at[idx, 'agenda_efetivada'] = 'sugerida'

    agendas[tecnico] = agenda

    return True
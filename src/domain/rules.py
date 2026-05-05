def tecnico_liberado_para_cliente(tecnico, cliente, lib_df):
    try:
        val = lib_df.loc[lib_df['cliente'] == cliente, tecnico].values
        return len(val) > 0 and str(val[0]).lower() == 'liberado'
    except Exception:
        return False
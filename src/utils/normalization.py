def normalize_text(s):
    return (
        str(s)
        .strip()
        .lower()
        .replace("não", "nao")
        .replace("nâo", "nao")
        .replace("nan", "nao")
    )
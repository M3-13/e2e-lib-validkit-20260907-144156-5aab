def mask_secret(text: str, keep: int = 4) -> str:
    if not isinstance(text, str):
        raise TypeError("mask_secret() expects text to be a string")
    if isinstance(keep, bool) or not isinstance(keep, int):
        raise TypeError("mask_secret() expects keep to be an integer")
    if keep < 0:
        raise ValueError("mask_secret() expects keep to be non-negative")

    if len(text) <= keep:
        return "*" * len(text)
    return "*" * (len(text) - keep) + text[len(text) - keep :]

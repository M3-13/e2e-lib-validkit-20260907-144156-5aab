def mask_secret(text: str, keep: int = 4) -> str:
    if not isinstance(text, str):
        raise TypeError("mask_secret() expects text to be a string")
    if isinstance(keep, bool) or not isinstance(keep, int):
        raise TypeError("mask_secret() expects keep to be an integer")
    if keep < 0:
        raise ValueError("mask_secret() expects keep to be non-negative")

    n = len(text)
    if n <= keep:
        return "*" * n
    if n > 2 * keep:
        visible = max(0, keep - 1)
        return "*" * (n - visible) + text[n - visible :]
    visible = n - keep
    return "*" * visible + text[n - visible :]

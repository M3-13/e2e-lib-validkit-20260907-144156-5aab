import unicodedata


def strip_accents(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("strip_accents() expects a string argument")

    normalized = unicodedata.normalize("NFD", text)
    return "".join(char for char in normalized if unicodedata.category(char) != "Mn")

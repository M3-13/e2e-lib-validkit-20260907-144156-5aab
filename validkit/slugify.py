import re
import unicodedata


def slugify(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("slugify() expects a string argument")

    decomposed = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(c for c in decomposed if not unicodedata.combining(c))
    lowered = ascii_text.lower()
    hyphenated = re.sub(r"[^a-z0-9]+", "-", lowered)
    return hyphenated.strip("-")

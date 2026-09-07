import re

_IBAN_PATTERN = re.compile(r"[A-Z]{2}[0-9]{2}[A-Z0-9]+")

_MAX_IBAN_LENGTH = 34
_MIN_IBAN_LENGTH = 15


def is_valid_iban(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("is_valid_iban expects a string")

    compact = text.replace(" ", "").upper()

    if len(compact) > _MAX_IBAN_LENGTH:
        raise ValueError("is_valid_iban: IBAN exceeds the maximum length of 34 characters")

    if len(compact) < _MIN_IBAN_LENGTH or not _IBAN_PATTERN.fullmatch(compact):
        return False

    rearranged = compact[4:] + compact[:4]
    digits = "".join(str(ord(ch) - ord("A") + 10) if ch.isalpha() else ch for ch in rearranged)

    remainder = 0
    for digit in digits:
        remainder = (remainder * 10 + int(digit)) % 97

    return remainder == 1

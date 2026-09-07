import re

_EMAIL_RE = re.compile(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

MAX_EMAIL_LENGTH = 254


def is_valid_email(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("is_valid_email() requires a string argument")
    if len(text) > MAX_EMAIL_LENGTH:
        raise ValueError("is_valid_email() rejects input longer than 254 characters")
    return _EMAIL_RE.fullmatch(text) is not None

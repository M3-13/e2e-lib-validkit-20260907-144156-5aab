import re

COUNTRY_CODES = {"DE": "49", "AT": "43", "CH": "41"}

_NON_DIGITS = re.compile(r"\D")


def normalize_phone(text: str, country_code: int | str) -> str:
    if not isinstance(text, str):
        raise TypeError("normalize_phone: text must be a string")

    if isinstance(country_code, int):
        digits = str(country_code)
    elif isinstance(country_code, str):
        code = country_code.strip()
        if code.startswith("+"):
            code = code[1:]
        digits = COUNTRY_CODES.get(code.upper(), code)
    else:
        raise TypeError("normalize_phone: country_code must be an int or str")

    if not digits.isdigit():
        raise ValueError("normalize_phone: invalid country code")

    national = _NON_DIGITS.sub("", text)
    if not national:
        raise ValueError("normalize_phone: phone number contains no digits")

    if national.startswith("0"):
        national = national[1:]
    if not national:
        raise ValueError("normalize_phone: phone number has no national number")

    if len(digits) + len(national) > 15:
        raise ValueError("normalize_phone: phone number exceeds 15 digits")

    return "+" + digits + national

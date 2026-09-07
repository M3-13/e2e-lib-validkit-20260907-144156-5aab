def luhn_check(digits: str) -> bool:
    if not isinstance(digits, str):
        raise TypeError("luhn_check: input must be a string")
    if digits == "":
        raise ValueError("luhn_check: input must not be empty")
    if not digits.isascii() or not digits.isdigit():
        raise ValueError("luhn_check: input must contain only digits")

    total = 0
    for index, char in enumerate(reversed(digits)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0

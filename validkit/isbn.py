def is_valid_isbn13(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("is_valid_isbn13() expects a string")

    digits = text.replace("-", "").replace(" ", "")

    if len(digits) > 13:
        raise ValueError("is_valid_isbn13() input exceeds the maximum length of 13 digits")

    if len(digits) != 13 or not digits.isdigit():
        return False

    total = sum(int(digit) * (1 if index % 2 == 0 else 3) for index, digit in enumerate(digits))
    return total % 10 == 0

import pytest

from validkit.phone import normalize_phone


def test_normalize_with_int_country_code():
    assert normalize_phone("030 1234 567", 49) == "+49301234567"


def test_normalize_with_two_letter_country_code():
    assert normalize_phone("(030) 1234-567", "DE") == "+49301234567"


def test_normalize_with_digit_string_country_code():
    assert normalize_phone("030 1234 567", "49") == "+49301234567"


def test_normalize_with_plus_prefixed_country_code():
    assert normalize_phone("030 1234 567", "+49") == "+49301234567"


def test_normalize_with_lowercase_country_code():
    assert normalize_phone("030 1234 567", "de") == "+49301234567"


def test_removes_leading_zero_of_national_number():
    assert normalize_phone("0301234567", "DE") == "+49301234567"


def test_ignores_separator_characters():
    assert normalize_phone("+030.1234-567", 49) == "+49301234567"


def test_more_than_15_digits_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("1234567890123456", 49)


def test_total_digits_exceeding_15_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("123456789012345", 49)


def test_exactly_15_total_digits_is_allowed():
    assert normalize_phone("1234567890123", 49) == "+491234567890123"


def test_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone(301234567, 49)


def test_invalid_country_code_type_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone("030 1234 567", 49.0)


def test_unknown_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("030 1234 567", "XX")


def test_empty_text_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("", 49)


def test_text_without_digits_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("abc", 49)


def test_error_message_does_not_contain_input():
    with pytest.raises(ValueError) as excinfo:
        normalize_phone("1234567890123456", 49)
    assert "1234567890123456" not in str(excinfo.value)

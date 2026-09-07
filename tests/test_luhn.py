import pytest

from validkit.luhn import luhn_check


def test_luhn_check_valid_number():
    assert luhn_check("79927398713") is True


def test_luhn_check_invalid_number():
    assert luhn_check("79927398710") is False


def test_luhn_check_empty_input_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("")


def test_luhn_check_non_digit_input_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("12a4")


def test_luhn_check_non_string_raises_type_error():
    with pytest.raises(TypeError):
        luhn_check(79927398713)


def test_luhn_check_single_digit():
    assert luhn_check("0") is True


def test_luhn_check_single_non_zero_digit():
    assert luhn_check("5") is False

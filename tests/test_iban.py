import pytest

from validkit import is_valid_iban


def test_valid_german_iban_returns_true():
    assert is_valid_iban("DE44 5001 0517 5407 3249 31") is True


def test_lowercase_iban_is_accepted():
    assert is_valid_iban("de44 5001 0517 5407 3249 31") is True


def test_tampered_check_digits_return_false():
    assert is_valid_iban("DE45 5001 0517 5407 3249 31") is False


def test_more_than_34_characters_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_iban("DE44" + "0" * 31)


def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_iban(12345)


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_iban(None)


def test_implausible_format_returns_false():
    assert is_valid_iban("123456789012345") is False
    assert is_valid_iban("") is False
    assert is_valid_iban("D44X") is False


def test_error_messages_do_not_contain_input_values():
    too_long = "A" * 35
    with pytest.raises(ValueError) as excinfo:
        is_valid_iban(too_long)
    assert too_long not in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo:
        is_valid_iban(12345)
    assert "12345" not in str(excinfo.value)

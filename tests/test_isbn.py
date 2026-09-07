import pytest

from validkit.isbn import is_valid_isbn13


def test_valid_isbn13_with_separators():
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn13_without_separators():
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn13_with_spaces():
    assert is_valid_isbn13("978 3 16 148410 0") is True


def test_invalid_check_digit_returns_false():
    assert is_valid_isbn13("978-3-16-148410-1") is False


def test_twelve_digits_returns_false():
    assert is_valid_isbn13("978316148410") is False


def test_fourteen_digits_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("97831614841000")


def test_non_digit_characters_return_false():
    assert is_valid_isbn13("978-3-16-14841X-0") is False


def test_empty_string_returns_false():
    assert is_valid_isbn13("") is False


def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(9783161484100)


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(None)


def test_error_messages_do_not_leak_input():
    with pytest.raises(TypeError) as excinfo:
        is_valid_isbn13(123)
    assert "123" not in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        is_valid_isbn13("97831614841000")
    assert "97831614841000" not in str(excinfo.value)

import pytest

from validkit.email import is_valid_email


def test_valid_email_returns_true():
    assert is_valid_email("a.b@example.com") is True


def test_email_without_dot_in_domain_is_invalid():
    assert is_valid_email("a@b") is False


def test_email_with_single_char_tld_is_invalid():
    assert is_valid_email("a@b.c") is False


def test_empty_string_is_invalid():
    assert is_valid_email("") is False


def test_email_with_exactly_254_chars_is_valid():
    email = "a" * 64 + "@" + "b" * 186 + ".co"
    assert len(email) == 254
    assert is_valid_email(email) is True


def test_email_longer_than_254_chars_raises_value_error():
    email = "a" * 64 + "@" + "b" * 187 + ".co"
    assert len(email) == 255
    with pytest.raises(ValueError):
        is_valid_email(email)


@pytest.mark.parametrize("value", [None, 123, 3.14, b"a@b.c", ["a@b.c"]])
def test_non_string_raises_type_error(value):
    with pytest.raises(TypeError):
        is_valid_email(value)


def test_type_error_message_names_function_and_cause():
    with pytest.raises(TypeError) as excinfo:
        is_valid_email(123)
    message = str(excinfo.value)
    assert "is_valid_email" in message
    assert "123" not in message


def test_value_error_message_does_not_leak_input():
    email = "x" * 300
    with pytest.raises(ValueError) as excinfo:
        is_valid_email(email)
    message = str(excinfo.value)
    assert "is_valid_email" in message
    assert email not in message

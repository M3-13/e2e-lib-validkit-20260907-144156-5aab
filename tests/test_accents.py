import pytest

from validkit import strip_accents


def test_strip_accents_removes_diacritics_keeps_other_characters():
    assert strip_accents("München — café") == "Munchen — cafe"


def test_strip_accents_empty_string():
    assert strip_accents("") == ""


def test_strip_accents_text_without_diacritics_is_unchanged():
    assert strip_accents("Hello, world! 123") == "Hello, world! 123"


def test_strip_accents_non_string_raises_type_error():
    with pytest.raises(TypeError):
        strip_accents(123)


def test_strip_accents_type_error_message_does_not_leak_input():
    with pytest.raises(TypeError) as exc_info:
        strip_accents("München — café".encode())
    assert "München" not in str(exc_info.value)

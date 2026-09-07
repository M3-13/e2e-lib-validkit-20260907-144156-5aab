import pytest

from validkit.masking import mask_secret


def test_masks_all_but_last_keep_chars():
    assert mask_secret("geheim123", keep=4) == "******123"


def test_masks_entire_text_when_shorter_than_keep():
    assert mask_secret("ab", keep=4) == "**"


def test_default_keep_is_four():
    assert mask_secret("geheim") == "**im"


def test_keep_zero_masks_everything():
    assert mask_secret("geheim", keep=0) == "******"


def test_keep_equal_to_length_masks_everything():
    assert mask_secret("geheim", keep=6) == "******"


def test_empty_text():
    assert mask_secret("") == ""


def test_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret(12345, keep=4)


def test_non_integer_keep_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret("geheim", keep="4")


def test_float_keep_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret("geheim", keep=4.0)


def test_negative_keep_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("geheim", keep=-1)


def test_type_error_message_does_not_leak_input_value():
    with pytest.raises(TypeError) as exc_info:
        mask_secret("geheim123", keep="4")
    assert "geheim123" not in str(exc_info.value)
    assert "4" not in str(exc_info.value)


def test_value_error_message_does_not_leak_input_value():
    with pytest.raises(ValueError) as exc_info:
        mask_secret("geheim123", keep=-4)
    assert "geheim123" not in str(exc_info.value)
    assert "-4" not in str(exc_info.value)

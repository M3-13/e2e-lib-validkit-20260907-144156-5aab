import pytest

from validkit.clamp import clamp


def test_clamp_value_within_bounds_returns_unchanged():
    assert clamp(5, 0, 10) == 5


def test_clamp_value_below_low_returns_low():
    assert clamp(-3, 0, 10) == 0


def test_clamp_value_above_high_returns_high():
    assert clamp(42, 0, 10) == 10


def test_clamp_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(1, 5, 3)


def test_clamp_returns_float_when_any_argument_is_float():
    assert clamp(3.5, 0.0, 10.0) == 3.5
    assert clamp(-1.5, 0, 10) == 0
    assert clamp(50.0, 0, 10) == 10


def test_clamp_non_numeric_value_raises_type_error():
    with pytest.raises(TypeError):
        clamp("5", 0, 10)


def test_clamp_non_numeric_low_raises_type_error():
    with pytest.raises(TypeError):
        clamp(5, "0", 10)


def test_clamp_non_numeric_high_raises_type_error():
    with pytest.raises(TypeError):
        clamp(5, 0, "10")


def test_clamp_boolean_argument_raises_type_error():
    with pytest.raises(TypeError):
        clamp(True, 0, 10)


def test_clamp_value_error_message_does_not_contain_input_values():
    with pytest.raises(ValueError) as excinfo:
        clamp(1, 5, 3)
    message = str(excinfo.value)
    assert "1" not in message
    assert "5" not in message
    assert "3" not in message


def test_clamp_type_error_message_does_not_contain_input_values():
    with pytest.raises(TypeError) as excinfo:
        clamp("secret", 0, 10)
    assert "secret" not in str(excinfo.value)

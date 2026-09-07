def clamp(value: int | float, low: int | float, high: int | float) -> int | float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("clamp() erwartet numerische Argumente (int oder float)")
    if isinstance(low, bool) or not isinstance(low, (int, float)):
        raise TypeError("clamp() erwartet numerische Argumente (int oder float)")
    if isinstance(high, bool) or not isinstance(high, (int, float)):
        raise TypeError("clamp() erwartet numerische Argumente (int oder float)")
    if low > high:
        raise ValueError("clamp(): low darf nicht größer als high sein")
    return max(low, min(value, high))

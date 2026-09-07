import validkit

EXPECTED_NAMES = {
    "is_valid_email",
    "luhn_check",
    "is_valid_iban",
    "is_valid_isbn13",
    "normalize_phone",
    "strip_accents",
    "mask_secret",
    "slugify",
    "clamp",
}


def test_all_contains_exactly_the_nine_names():
    assert len(validkit.__all__) == 9
    assert set(validkit.__all__) == EXPECTED_NAMES


def test_all_nine_names_are_importable():
    for name in EXPECTED_NAMES:
        assert callable(getattr(validkit, name))

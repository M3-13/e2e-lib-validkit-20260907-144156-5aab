import pytest

from validkit.slugify import slugify


def test_slugify_accents_and_punctuation():
    assert slugify("Héllo, Wörld!") == "hello-world"


def test_slugify_multiple_special_characters():
    assert slugify("Hello---World") == "hello-world"
    assert slugify("foo***bar///baz") == "foo-bar-baz"


def test_slugify_leading_and_trailing_hyphens():
    assert slugify("-hello-world-") == "hello-world"
    assert slugify("  --hello--  ") == "hello"


def test_slugify_empty_string():
    assert slugify("") == ""


def test_slugify_umlauts_and_spaces():
    assert slugify("Über München") == "uber-munchen"


@pytest.mark.parametrize("value", [None, 42, 3.14, ["Héllo"], {"a": 1}])
def test_slugify_non_string_raises_type_error(value):
    with pytest.raises(TypeError):
        slugify(value)

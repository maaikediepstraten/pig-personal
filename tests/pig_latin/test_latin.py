"""Unit tests for the demo module."""

from pig_latin.latin import _convert_word, pig_latin


def test_convert_word():
    """Test convert_word function."""
    assert _convert_word("Hello") == "Ellohay"


def test_pig_latin():
    """Test pig_latin function."""
    assert pig_latin("Hello World!") == "Ellohay Orldway!"

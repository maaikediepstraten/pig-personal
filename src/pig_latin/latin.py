"""Module for Pig Latin functions."""

import re
import sys


def _convert_word(word: str) -> str:
    """Convert a single word to Pig Latin.

    Example: Hello => Ellohay

    Parameters
    ----------
    word : str
        The word to be converted.

    Returns
    -------
    str
        The converted word.
    """
    return (word[1:] + word[0] + "ay").capitalize()


def pig_latin(text: str) -> str:
    """Convert text into Pig Latin.

    Parameters
    ----------
    text : str
        The text to be converted.

    Returns
    -------
    str
        The converted text.
    """
    result = []

    match = re.split(r"([?!\., ])", text)
    for token in match:
        if token not in "?!., ":
            token = _convert_word(token)
        result.append(token)

    return "".join(result)


def main() -> None:
    """Main function to run the Pig Latin conversion."""
    message = "Hello world!"
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    print(pig_latin(message))


if __name__ == "__main__":
    main()

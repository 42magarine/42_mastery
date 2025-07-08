#!/usr/local/bin/python3

import sys


def count_characters(text: str) -> dict:
    """
    Count different types of characters in the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with counts for each character type.
    """
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    result = {
        "upper": 0,
        "lower": 0,
        "digit": 0,
        "punct": 0,
        "space": 0,
        "total": len(text),
    }

    for char in text:
        if char.isupper():
            result["upper"] += 1
        elif char.islower():
            result["lower"] += 1
        elif char.isdigit():
            result["digit"] += 1
        elif char.isspace():
            result["space"] += 1
        elif char in punctuation:
            result["punct"] += 1

    return result


def print_result(counts: dict) -> None:
    """
    Print the character statistics.

    Args:
        counts (dict): Dictionary containing character counts.
    """
    print(f"The text contains {counts['total']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punct']} punctuation marks")
    print(f"{counts['space']} spaces")
    print(f"{counts['digit']} digits")


def main() -> None:
    """
    Get input, count characters, and print result.
    """
    try:
        args = sys.argv[1:]

        if len(args) == 0:
            user_input = input("What is the text to count?\n")
        elif len(args) == 1:
            user_input = args[0]
        else:
            raise AssertionError("more than one argument is provided")

        counts = count_characters(user_input)
        print_result(counts)

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

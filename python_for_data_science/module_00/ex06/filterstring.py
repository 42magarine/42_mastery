#!/usr/local/bin/python3

import sys
from ft_filter import ft_filter


def main() -> None:
    """
    Main function to validate arguments and print filtered words.
    """
    try:
        args = sys.argv[1:]

        if len(args) != 2:
            raise AssertionError("the arguments are bad")

        list_of_words = args[0].split()

        try:
            length = int(args[1])
        except ValueError:
            raise AssertionError("the arguments are bad")

        print(list(ft_filter(lambda word: len(word) > length, list_of_words)))

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()

#!/usr/local/bin/python3

import sys


def main() -> None:
    """
    Encode a string into Morse Code.
    """
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. ",
                    "0": "----- "
                    }

    args = sys.argv[1:]

    if len(args) != 1:
        raise AssertionError("the arguments are bad")

    text_string = args[0].upper()

    if not all(char in NESTED_MORSE for char in text_string):
        raise AssertionError("the arguments are bad")

    mouse_string = "".join(NESTED_MORSE[char] for char in text_string).strip()
    print(str(mouse_string))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")

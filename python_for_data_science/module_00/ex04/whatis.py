#!/usr/bin/env python

import sys

try:
    args = sys.argv[1:]

    if len(args) == 0:
        sys.exit()
    if len(args) > 1:
        raise AssertionError("more than one argument is provided")

    try:
        number = int(args[0])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as error:
    print(f"AssertionError: {error}")

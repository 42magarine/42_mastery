def ft_tqdm(lst: range) -> None:
    """
    Prints a progress bar while iterating over a range.

    Args:
        lst (range): The range to iterate over.
    """
    total = len(lst)
    bar_length = 85    # Terminal width 125

    for index in lst:
        percent = int((index + 1) / total * 100)

        filled_length = int(bar_length * percent / 100)
        bar = "█" * filled_length + " " * (bar_length - filled_length)

        print(f"\r{percent:3}%|{bar}| {index + 1}/{total}", end="", flush=True)
        yield index


# Explanation of print options:
# \r         → Carriage return: moves the cursor to the beginning of the line.
# end=""     → Prevents print() from adding a newline after each call.
# flush=True → Forces the output to be written immediately.

# https://www.tutorialspoint.com/python/python_generators.htm
# https://www.tutorialspoint.com/python/python_yield_keyword.htm

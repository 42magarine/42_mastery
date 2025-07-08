#!/usr/local/bin/python3

import time
from datetime import date

current_time = time.time()
formatted_time = f"{current_time:,.4f}"
scientific_time = f"{current_time:.2e}"
print(
    f"Seconds since January 1, 1970: {formatted_time} or {scientific_time} "
    "in scientific notation"
)

current_date = date.today()
formatted_date = current_date.strftime("%b %d %Y")
print(formatted_date)

# https://docs.python.org/3/library/time.html#functions
# https://docs.python.org/3/library/datetime.html#date-objects
# https://docs.python.org/3/library/string.html#format-specification-mini-language

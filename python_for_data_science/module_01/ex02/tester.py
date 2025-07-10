#!/usr/local/bin/python3

from load_image import ft_load

try:
    print(ft_load("landscape.jpg"))
except Exception as error:
    print(error)

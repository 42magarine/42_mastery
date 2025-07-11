#!/usr/bin/env python

from load_image import ft_load

try:
    print(ft_load("landscape.jpg"))
except Exception as error:
    print(error)

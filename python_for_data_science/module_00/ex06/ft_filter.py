def ft_filter(function, iterable):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function:
        return (item for item in iterable if function(item))
    return (item for item in iterable if item)


# https://docs.python.org/3/library/functions.html#filter
# https://www.tutorialspoint.com/python/python_list_comprehension.htm

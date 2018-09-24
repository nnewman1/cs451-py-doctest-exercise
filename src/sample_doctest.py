# sample_doctest.py
# Using unit tests included in docstrings 

def pow_of_two(x):
    """Return x to the power of 2.

    >>> pow_of_two(4)
    16
    >>> pow_of_two(-2)
    4
    """
    return x**2

def float_div_by_two(x):
    """Return x divided by 2 in floating point precision.

    >>> float_div_by_two(49)
    24.5
    >>> float_div_by_two(48)
    24.0
    """
    return x / 2.0

def get_evens(n):
    """Return the first n even numbers as a list.

    >>> get_evens(10)
    [0, 2, 4, 6, 8]
    """
    return list(range(0, n, 2))

def get_mid(data):
    """Return the midpoint value in data.
    >>> get_mid([0, 2, 4, 6, 8])
    4
    """
    return data[len(data)//2]

def get_last_half(data):
    """Return the values in the last half of data (slice) as a list.
    >>> get_last_half([0, 2, 4, 6, 8])
    [4, 6, 8]
    """
    return list(data[2:])

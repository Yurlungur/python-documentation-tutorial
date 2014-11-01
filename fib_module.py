#!/usr/bin/env python

"""
Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
Time-stamp: <2014-11-01 19:01:19 (jonah)>

A Fibonacci program contained in a Python module to make it more
efficient.

For an explanation, see:
<http://functionspace.org/articles/32/Fibonacci-series-and-Dynamic-programming>
"""

import sys


# The first N fibonacci numbers, where n is the length of the list
__fib_numbers=[1,1]


def dumb_fib(n):
    """
    Returns the Nth Fibonacci number, but without dynamic
    programming. Dumb code.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return dumb_fib(n-2) + dumb_fib(n-1)

    
def smart_fib(n):
    """
    Returns the Nth Fibonacci number, indexed from 0. Uses "dynamic
    programming" to cache data for later.
    """
    assert type(n) == int
    assert n >= 0
    if n < len(__fib_numbers):
        return __fib_numbers[n]
    __fib_numbers.append(smart_fib(n-1) + smart_fib(n-2))
    return __fib_numbers[-1]

if __name__ == "__main__":
    print smart_fib(int(sys.argv[1]))

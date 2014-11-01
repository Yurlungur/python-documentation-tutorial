#!/usr/bin/env python

"""
row_echo.py
Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
Time-stamp: <2014-11-01 18:23:03 (jonah)>

This simple script shows how one can use command line arguments.
"""

import sys

if __name__ == "__main__":
    print "This file's name is: {}".format(sys.argv[0])
    print "The command line arguments are:"
    for arg in sys.argv[1:]:
        print arg

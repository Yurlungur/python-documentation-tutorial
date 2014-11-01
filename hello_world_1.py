#!/usr/bin/env python

"""
hello_world_1.py
Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
Time-stamp: <2014-11-01 18:19:14 (jonah)>

This is the first Python example script that describes how to interact
with Python files.

A string that is unassigned to a variable can be used (in certain
contexts) as a comment. It doubles as the documentation when you call
the help() function via the Python interpreter. This is called a
'docstring.'

I use three quotation marks for this string because strings with three
quotation marks faithfully reproduce whitespace.
"""

hellostring1="Hello world!"
hellostring2="""
Hello...
World!
"""

def hello_world_1():
    """
    This function prints 'Hello world!' to the screen.

    This version has no whitespace.
    """
    print hellostring1

def hello_world_2():
    """
    This function prints 'Hello... World!' to the screen, but with
    whitespace!
    """
    print hellostring2

hello_world_1()


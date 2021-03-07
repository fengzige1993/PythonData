"""
python内置函数instance()
"""


class A:
    pass


class B(A):
    pass


if isinstance(A(), A):
    returen True # returns True
type(A()) == A  # returns True
isinstance(B(), A)  # returns True
type(B()) == A  # returns False
"""
pep3110.py
Created by Peng Xiao on 2018-07-23. xiaoquwl@gmail.com
"""

from __future__ import print_function


def compute(a, b):
    try:
        return a / b
    except (TypeError, ZeroDivisionError, Exception) as e:
        print('has error')
        print(type(e))
        print(e)

if __name__ == "__main__":
    compute(1, 0)

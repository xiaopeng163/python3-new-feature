"""
pep435.py
Created by Peng Xiao on 2018-07-13. xiaoquwl@gmail.com
"""

from enum import Enum


class Color(Enum):
    RED = 1
    YELLOW = 2
    BLUE = 3


# iterator
for col in Color:
    print(col)
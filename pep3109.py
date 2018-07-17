"""
pep3109.py
Created by Peng Xiao on 2018-07-23. xiaoquwl@gmail.com
"""

from __future__ import print_function
from exceptions import Exception


class MyException(Exception):
    pass

raise MyException()
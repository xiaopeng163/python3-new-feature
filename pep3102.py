"""
pep3102.py
Created by Peng Xiao on 2018-07-15. xiaoquwl@gmail.com
"""

def foo1(x, y, z=0):
    return x + y + z


print(foo1(1, 2))
print(foo1(1, 2, 3))
print(foo1(x=1, 2))
print(foo1(x=1, y=2))


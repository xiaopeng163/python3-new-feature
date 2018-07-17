"""
pep3101.py
Created by Peng Xiao on 2018-07-15. xiaoquwl@gmail.com
"""

# basic c like formatting

a = '%s %d %d'
assert a % ('ljs', 22, 75) == 'ljs 22 75'   # format by position

a = {"name":'ljs',"age":22,'weight':75}
assert "%(name)s %(age)d %(weight)d;" % a == "ljs 22 75;"   # format by keyword

a = 1.23456
assert "%f" % a == "1.234560"
assert "%3f" % a == "1.234560"
assert "%10f" % a == "  1.234560"  # lenth = 10
assert "%.10f" % a == '1.2345600000' 

"""
pep450.py
Created by Peng Xiao on 2018-07-14. xiaoquwl@gmail.com
"""

scores = [92, 88, 80, 68, 52]

def my_mean(data):
    return sum(data) / len(data)


def my_variance(data):
    _mean = my_mean(data)
    return sum([ (x - _mean) ** 2 for x in data]) / len(data)


def my_standard_deviation(data):
    import math
    return math.sqrt(my_variance(data))

print('mean is:', my_mean(scores))
print('variance is:', my_variance(scores))
print('standard deviation is:', my_standard_deviation(scores))


print('Let check with python standard statistic standard library')

from statistics import mean, pvariance, pstdev

print('mean is:', mean(scores))
print('variance is:', pvariance(scores))
print('standard deviation is:', pstdev(scores))

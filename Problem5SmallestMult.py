__author__ = 'Richard'

"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


from fractions import gcd
def lcm(a, b):
    return a*b//gcd(a, b)

from functools import reduce
print(reduce(lcm, range(1, 10+1)))
print(reduce(lcm, range(1, 20+1)))



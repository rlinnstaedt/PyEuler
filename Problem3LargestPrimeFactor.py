import math


__author__ = 'Richard'

"""The prime factors of 13195 are 5, 7, 13, 29.

What is the largest prime factor of the number 600851475143 ?"""


def is_prime(x):

    if x <= 1 or x % 2 == 0:
        return 0

    check = 3
    maxneeded = x
    while check < maxneeded + 1:
        maxneeded = x/check
        if x % check == 0:
            return 0
        check += 1
    return 1


def factorization(n):

    factors = []
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i is 0:
            if is_prime(i) == 1:
                factors.append(i)

    print("Max prime for ", n, "is: ", factors.pop())

factorization(13195)
factorization(600851475143)

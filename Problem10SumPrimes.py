import math

__author__ = 'Richard'

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""


def is_prime(x):

    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def sum_primes(n):  # n is the upper limit for the list of primes

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)

    print("The sum of primes up to:", n, "is:", sum(primes))

sum_primes(10)
sum_primes(2000000)

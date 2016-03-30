import math
import sys

_author__ = 'Richard'

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

def is_prime(x):

    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True



def nth_prime(n):

    # upper_bound = int(n*math.log(n) + math.log(math.log(n)-0.9385))

    count = 0
    primes = 1
    while count < n:
        primes += 1
        if is_prime(primes):
            count += 1
    return primes


import time
start_time = time.time()
print(nth_prime(6))
print(nth_prime(10001))
print(time.time() - start_time)

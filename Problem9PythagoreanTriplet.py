

__author__ = 'Richard'


"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""


def pythagorean_triplet(n):

    for b in range(1, n):
        for a in range(1, n - b):
            c = n - a - b
            if b**2 + a**2 == c ** 2:
                if b > a:
                    print("a:", a, "b:", b, "c:", c, "abc:", a*b*c)

pythagorean_triplet(1000)
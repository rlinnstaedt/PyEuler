__author__ = 'Richard'



def is_palindrome(multiple):

    return str(multiple) == str(multiple)[::-1]


palindromes = []
for x in range(100, 1000, 1):
    for y in range(100, 1000, 1):

        if is_palindrome(x * y):
            palindromes.append(x * y)

print(sorted(palindromes)[-1])



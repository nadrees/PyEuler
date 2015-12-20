'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

from Generators import Primes
from itertools import takewhile

num = 600851475143

largestPrime = -1

while num >= 2:
    for x in Primes():
        if num % x == 0:
            num /= x
            if x > largestPrime:
                largestPrime = x
            break

print(largestPrime)
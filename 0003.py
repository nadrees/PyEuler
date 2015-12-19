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
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
'''

from Generators import Primes

n = 10001
primes = Primes()
p = None

for i in range(n):
    p = primes.__next__()

print(p)
from itertools import count

def Fibonacci(startWithRepeatingOnes = False):
    '''Generator for the Fibonacci sequence'''
    n1 = 1
    yield n1
    n2 = 1 if startWithRepeatingOnes else 2
    yield n2
    while True:
        n3 = n1 + n2
        yield n3
        n1 = n2
        n2 = n3

def Primes():
    '''Generator for prime numbers'''
    D = {} # map each composite integer to its first found prime factor
    for q in count(2): #q gets 2, 3, 4, 5, ...
        p = D.pop(q, None)
        if p is None:
            # q not a key in D, therefore q is prime
            yield q
            # mark q^2 as not prime, with q as first prime factor
            D[q*q] = q
        else:
            # let x <- smallest (N*p)+q which wasn't yet known to be composite
            # we just learned x is composite, with p first-found prime factor,
            # since p is the first-found prime factor of q -- find and mark it
            x = p + q
            while x in D:
                x += p
            D[x] = p
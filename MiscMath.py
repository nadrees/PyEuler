from Generators import Primes

def GetFactors(n):
    '''Returns all factors of n greater than 0'''
    if n < 1: 
        return []
    return [x for x in range(1, n + 1) if n % x == 0]

def GetPrimeFactors(n):
    '''
    Returns all prime factors for n.

    Return value is a dictionary of {prime: cardinality}. The cardinality is the number of times
    the prime appears in the factor tree.

    Ex: The prime factors of 72 are [2, 2, 2, 3, 3], and the return value of this function would be {2: 3, 3: 2}.
    '''
    primeFactors = {}
    while n >= 2:
        for x in Primes():
            if n % x == 0:
                n /= x
                if x in primeFactors:
                    primeFactors[x] += 1
                else:
                    primeFactors[x] = 1
                break
    return primeFactors

def GetCountOfFactors(n):
    '''Returns the number of factors of n'''
    primeFactors = GetPrimeFactors(n)
    if len(primeFactors) == 0:
        return 0
    else:
        numFactors = 1
        for c in map(lambda cardinality: cardinality + 1, primeFactors.values()):
            numFactors *= c
        return numFactors

if __name__ == '__main__':
    import unittest
    
    class Tests(unittest.TestCase):
        def test_GetFactors(self):
            cases = [{'n': -1, 'answer': []},
                     {'n': 0, 'answer': []},
                     {'n': 1, 'answer': [1]},
                     {'n': 2, 'answer': [1, 2]},
                     {'n': 28, 'answer': [1,2,4,7,14,28]},
                     {'n': 72, 'answer': [1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72]}]
            for case in cases:
                n = case['n']
                expected = case['answer']
                with self.subTest(n=n, expected=expected):
                    answer = GetFactors(n)
                    self.assertEqual(expected, answer)

        def test_GetPrimeFactors(self):
            cases = [{'n': -1, 'answer': {}},
                     {'n': 1, 'answer': {}},
                     {'n': 72, 'answer': {2: 3, 3: 2}},
                     {'n': 13195, 'answer': {5: 1, 7: 1, 13: 1, 29: 1}}]
            for case in cases:
                n = case['n']
                expected = case['answer']
                with self.subTest(n=n, expected=expected):
                    answer = GetPrimeFactors(n)
                    self.assertEqual(expected, answer)

        def test_GetCountOfFactors(self):
            cases = [{'n': -1, 'answer': 0},
                     {'n': 1, 'answer': 0},
                     {'n': 72, 'answer': 12},
                     {'n': 28, 'answer': 6},
                     {'n': 13195, 'answer': 16}]
            for case in cases:
                n = case['n']
                expected = case['answer']
                with self.subTest(n=n, expected=expected):
                    answer = GetCountOfFactors(n)
                    self.assertEqual(expected, answer)

    unittest.main()
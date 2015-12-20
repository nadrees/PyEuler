from Generators import TriangleNumbers
from MiscMath import GetCountOfFactors

numDivisors = 500

for n in TriangleNumbers():
    if GetCountOfFactors(n) > numDivisors:
        print(n)
        break
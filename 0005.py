'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from itertools import count

nums = range(2, 21)

for x in count(2520):
    allDivisible = True
    for n in nums:
        if x % n != 0:
            allDivisible = False
            break
    if allDivisible:
        print(x)
        break
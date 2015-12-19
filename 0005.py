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
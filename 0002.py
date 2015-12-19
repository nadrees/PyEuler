from Generators import Fibonacci
from itertools import takewhile

nums = [x for x in takewhile(lambda x: x < 4000000, Fibonacci()) if x % 2 == 0]
answer = sum(nums)

print(answer)

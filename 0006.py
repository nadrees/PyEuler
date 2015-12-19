nums = range(1, 101)

sumOfSquares = sum([x * x for x in nums])
squareOfSums = sum(nums)**2

answer = squareOfSums - sumOfSquares

print(answer)
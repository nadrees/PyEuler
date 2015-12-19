limit = 1000
nums = [x for x in range(0, 1000) if x % 3 == 0 or x % 5 == 0]
answer = sum(nums)
print(answer)
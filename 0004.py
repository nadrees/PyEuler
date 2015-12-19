nums = range(999, 99, -1)

allProducts = [x * y for x in nums for y in nums]
palindromeProducts = [p for p in allProducts if str(p) == str(p)[::-1]]

answer = max(palindromeProducts)
print(answer)

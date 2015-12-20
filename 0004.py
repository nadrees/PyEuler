'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

nums = range(999, 99, -1)

allProducts = [x * y for x in nums for y in nums]
palindromeProducts = [p for p in allProducts if str(p) == str(p)[::-1]]

answer = max(palindromeProducts)
print(answer)

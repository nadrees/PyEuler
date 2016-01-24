'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

def num_to_text(n):
    if n == 1: return 'one'
    elif n == 2: return 'two'
    elif n == 3: return 'three'
    elif n == 4: return 'four'
    elif n == 5: return 'five'
    elif n == 6: return 'six'
    elif n == 7: return 'seven'
    elif n == 8: return 'eight'
    elif n == 9: return 'nine'
    elif n == 10: return 'ten'
    elif n == 11: return 'eleven'
    elif n == 12: return 'twelve'
    elif n == 13: return 'thirteen'
    elif n == 14: return 'fourteen'
    elif n == 15: return 'fifteen'
    elif n == 16: return 'sixteen'
    elif n == 17: return 'seventeen'
    elif n == 18: return 'eighteen'
    elif n == 19: return 'nineteen'
    elif n == 20: return 'twenty'
    elif n == 30: return 'thirty'
    elif n == 40: return 'forty'
    elif n == 50: return 'fifty'
    elif n == 60: return 'sixty'
    elif n == 70: return 'seventy'
    elif n == 80: return 'eighty'
    elif n == 90: return 'ninty'
    else:
        # build up spelling
        num = ''
        while n > 0:
            if n >= 1000:
                left_digit = int(n / 1000)
                num += num_to_text(left_digit) + ' thousand'
                n = n % 1000
                if n % 100 != 0:
                    num += ' ' 
            elif n >= 100:
                left_digit = int(n / 100)
                num += num_to_text(left_digit) + ' hundred'
                remainder = n % 100
                if remainder > 0:
                    num += ' and '
                n = remainder
            elif n >= 20:
                left_digit = int(n / 10) * 10 # get the tens num
                num += num_to_text(left_digit)
                remainder = n % 10
                if remainder > 0:
                    num += '-' + num_to_text(remainder)
                n = 0
            else:
                num += num_to_text(n)
                n = 0
        return num

num_in_text = [num_to_text(n) for n in range(1, 1001)]

letters = ''.join([x.replace(' ', '').replace('-', '') for x in num_in_text])

print(len(letters))
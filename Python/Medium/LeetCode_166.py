# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# If multiple answers are possible, return any of them.

# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num, den = abs(numerator), abs(denominator)
        num, res = num%den, str(num//den)
        d, s, c = {num: 0}, '', 1

        if numerator * denominator < 0:
            res = '-' + res

        while num:
            num *= 10
            s += str(num//den)
            num %= den

            if num not in d:
                d[num] = c
                c += 1
            else:
                s = s[0:den[num]] + '(' + s[den[num]:] + ')'
                break

        if len(s) > 0:
            res = res + '.' + s

        return res
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
# then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        rev = 0

        if x < 0:
            isNegative = True
            x = abs(x)

        while x > 0:
            last = x % 10
            x = x // 10

            if (rev > INT_MAX // 10 or (rev == INT_MAX // 10 and last > 7)):
                return 0

            rev = (rev * 10) + last

        return -rev if isNegative else rev
    


# Optimized and easy to unerstand solution
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)

        rev = int(str(x)[::-1])*sign
        if INT_MIN <= rev <= INT_MAX:
            return rev
        else:
            return 0
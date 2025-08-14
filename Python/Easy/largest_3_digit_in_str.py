# You are given a string num representing a large integer. An integer is good if it meets the following conditions:

# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.

# Note:

# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largeGoodInteger = ''

        # Iterate till 3rd last element
        for i in range(len(num)-2):
            if (num[i] == num[i+1] and num[i] == num[i+2]):
                # If above condition satisfy, then duplicate the current element thrice -> '7': '777'
                currentGoodInteger = num[i] * 3

                if largeGoodInteger == '' or currentGoodInteger > largeGoodInteger:
                    largeGoodInteger = currentGoodInteger

        return largeGoodInteger
    


# Alternate method single line check using RegEx
import re

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Using RegEx, we are checking for digits (\d) and from current position check consecutive 2 position for same match (\1\1)
        matched = re.findall(r'(\d)\1\1', num)
        
        # Return the max element that is repeated thrice and concat it thrice
        return max(matched, default='')*3
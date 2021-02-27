# We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

# Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.

# Example 1:
# Input: 20, Output: 6

# Explanation: 
# The confusing numbers are [6,9,10,16,18,19].
# 6 converts to 9.
# 9 converts to 6.
# 10 converts to 01 which is just 1.
# 16 converts to 91.
# 18 converts to 81.
# 19 converts to 61.


class Solution:
    def confusingNumber(self, num):
        confusingDigits = ['0', '1', '6', '8', '9']
        i = 0
        result = 0

        while i <= num:
            s = str(i)
            lst = s.split('')
            count = 0

            for j in lst:
                if j in confusingDigits:
                    count += 1
            if len(lst) == count:
                result += 1
            i += 1

        return result

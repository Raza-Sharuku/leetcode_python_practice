class Solution(object):
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        rev_num = int(str(x)[::-1])
        if sign < 0:
            rev_num *= -1 
        if (rev_num > 2**31 - 1 or rev_num < (-2)**31):
            return (0)
        return (rev_num)
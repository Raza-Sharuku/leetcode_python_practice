class Solution(object):
    def reverse(self, x):
        sign = 0
        if x < 0:
            sign = 1
            x *= -1
        rev_num = int(str(x)[::-1])
        if sign:
            rev_num *= -1 
        if (rev_num > 2**31 - 1 or rev_num < (-2)**31):
            return (0)
        return (rev_num)
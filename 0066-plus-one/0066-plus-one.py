class Solution(object):
    def plusOne(self, digits):

        return list(map(int, str(int("".join([str(x) for x in digits]))+1)))
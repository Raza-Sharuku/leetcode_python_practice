class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if (len(s) == 1):
            return (1)
        elif (len(s) == 0):
            return (0)
        tmp = []
        max = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[j] not in tmp:
                    tmp.append(s[j])
                else:
                    if (max < len(tmp)):
                        max = len(tmp)
                    tmp = []
                    break
        return (max)
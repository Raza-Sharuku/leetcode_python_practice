class Solution(object):
    def twoSum(self, nums, target):
        k = len(nums)
        for i in range(0, k - 1):
            for j in range(i + 1, k):
                if ((nums[i] + nums[j]) == target):
                    return list((i, j))
                
        
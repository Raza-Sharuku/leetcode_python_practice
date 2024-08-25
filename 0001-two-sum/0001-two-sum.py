class Solution(object):
    def twoSum(self, nums, target):
        if (len(nums) < 3):
            return list((0, 1))
        if (len(nums) == 3):
            if (nums[0] + nums[1] == target):
                return list((0, 1))
            elif (nums[0] + nums[2] == target):
                return list((0, 2))
            else :
                return list((1, 2))
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if ((nums[i] + nums[j]) == target):
                    return list((i, j))
                
        
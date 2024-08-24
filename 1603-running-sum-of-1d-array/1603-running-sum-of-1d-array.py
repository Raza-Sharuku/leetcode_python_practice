class Solution(object):
    def runningSum(self, nums):
        result = []
        for i in range(0,len(nums)):
            if (i >= 1):
                result.append(result[i - 1] + nums[i])
            else:
                result.append(nums[i])
        
        return result



        
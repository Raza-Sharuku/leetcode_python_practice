class Solution(object):#code
    def runningSum(self, nums):
        result = []
        length = len(nums)
        for i in range(0,length):
            if (i > 0):
                result.append(result[i - 1] + nums[i])
            else:
                result.append(nums[i])
        return result



        
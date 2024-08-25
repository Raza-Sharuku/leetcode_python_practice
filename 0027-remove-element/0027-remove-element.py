class Solution(object):
    def removeElement(self, nums, val):
        nums.sort()
        # print("first ->" , nums)
        # print("\n")
        i = 0
        while i < len(nums):
            if (nums[i] == val):
                j = i
                # print(i ,"[before] ---->" , nums)
                nums.pop(i)
                # print(i ,"[after ] ---->" , nums)

                if (i >= len(nums)):
                        return (len(nums))
            else:
                i += 1
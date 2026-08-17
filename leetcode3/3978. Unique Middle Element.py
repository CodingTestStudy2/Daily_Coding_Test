class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        ret = 0
        gijun = len(nums)//2
        gijun = nums[gijun]

        for n in nums:
            if n == gijun:
                ret+=1

        if ret == 1:
            return True
        else:
            return False

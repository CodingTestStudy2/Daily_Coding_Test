class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        i = len(nums) // 2
        a = nums[i]
        nums.remove(a)

        if a in nums:
            return False
        return True
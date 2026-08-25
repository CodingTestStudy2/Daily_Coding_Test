class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            if i % 2 == 0:
                result += nums[i]
            else:
                result -= nums[i]
        return result
        
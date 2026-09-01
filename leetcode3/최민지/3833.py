class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(0, n-1):
            if nums[i] > (sum(nums[i+1:]) / (n-(i+1))):
                result += 1
        return result
        
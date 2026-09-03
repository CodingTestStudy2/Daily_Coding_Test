class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(k):
            ans += nums[n-i-1] - nums[i]
        return ans

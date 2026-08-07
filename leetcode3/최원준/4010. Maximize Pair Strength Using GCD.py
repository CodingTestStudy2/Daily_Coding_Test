from math import gcd

class Solution:
    def maxPairStrength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                g = gcd(nums[i], nums[j])
                strength = (nums[i] * nums[j]) // (g * g)
                ans = max(ans, strength)
        return ans

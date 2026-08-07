import math

# 모든 조합으로 전부 구해본다
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = nums[i]
                b = nums[j]

                g = math.gcd(a, b)
                strength = (a * b) // (g * g)
                ans = max(strength, ans)

        return ans   
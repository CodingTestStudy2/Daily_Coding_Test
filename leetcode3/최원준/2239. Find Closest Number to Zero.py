class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        ans = -float('inf')
        diff = float('inf')
        for num in nums:
            if abs(num) == diff:
                ans = max(ans, num)
            elif abs(num) < diff:
                diff = abs(num)
                ans = num

        return ans

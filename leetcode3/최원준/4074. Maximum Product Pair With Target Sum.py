class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        max_product = -float('inf')
        ans = [-1, -1]
        n = len(nums)
        
        for i in range(n):
            for j in range(n):
                num1 = nums[i]
                num2 = nums[j]
                
                if num1 <= num2 or i == j:
                    continue
                if num1 * num2 > max_product and num1 + num2 == target:
                    max_product = num1 * num2
                    ans = [i, j]

        return ans

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        total_sum = 0
        n = len(nums)
        
        for i in range(n):
            if i - k >= 0 and nums[i] <= nums[i - k]:
                continue
            if i + k < n and nums[i] <= nums[i + k]:
                continue
            total_sum += nums[i]
            
        return total_sum
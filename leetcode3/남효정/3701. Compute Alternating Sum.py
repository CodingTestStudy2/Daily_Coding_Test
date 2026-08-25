class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even, odd = 0, 0

        for i in range(len(nums)):
            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]
        
        return even - odd
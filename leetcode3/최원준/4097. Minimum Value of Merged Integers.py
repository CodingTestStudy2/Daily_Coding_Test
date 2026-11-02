class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(0,n,2):
            ans = min( int(str(nums[i]) + str(nums[i+1])), ans )
        return ans

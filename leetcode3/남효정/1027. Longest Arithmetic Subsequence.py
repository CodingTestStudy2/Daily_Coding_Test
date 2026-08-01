'''
1. 아이디어 :
2. 시간복잡도 : O(n^2)
3. 자료구조/알고리즘 : DP
'''

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]

                dp[(i, diff)] = dp.get((j.diff), 1) + 1
        
        return max(dp.values())
        
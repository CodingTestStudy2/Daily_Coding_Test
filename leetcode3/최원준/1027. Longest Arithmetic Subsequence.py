from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 2

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

                if diff not in dp[j]:
                    dp[i][diff] = max(dp[i][diff], 2)
                else:
                    dp[i][diff] = max(
                        dp[i][diff],
                        dp[j][diff] + 1
                    )
                ans = max(ans, dp[i][diff])
        
        return ans

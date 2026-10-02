'''
1. 아이디어 :
    계단을 오르는 최소 비용. i번째 계단까지 올라오는 최소 비용을 dp[i]로 두면,
    i번째 계단은 i-1 또는 i-2에서 올 수 있으므로
    dp[i] = min(dp[i-1], dp[i-2]) + cost[i].
    마지막 계단(n-1)에 도착하지 않고 n-1을 건너뛸 수도 있으므로,
    정답은 마지막 두 칸 중 더 작은 값인 min(dp[n-1], dp[n-2]).
2. 시간복잡도 :
    o(n)
3. 자료구조/알고리즘 :
    dp, bottom-up
'''

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[n-1], dp[n-2])

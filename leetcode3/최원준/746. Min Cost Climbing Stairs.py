class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        n = len(cost)
        for i in range(2,n):
            cost[i] += min(cost[i-2], cost[i-1])
        return cost[-1]

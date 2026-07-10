class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        
        def split_cost(length):
            cost = 0
            while length > k:
                remain = length - k
                cost += k * remain
                length = remain
            return cost
        
        return split_cost(n) + split_cost(m)

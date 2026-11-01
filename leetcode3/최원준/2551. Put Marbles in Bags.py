class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        n = len(weights)
        pairs = []
        
        for i in range(n-1):
            pairs.append(weights[i] + weights[i+1])
    
        pairs.sort()
        min_value = 0
        max_value = 0
        
        for i in range(k-1):
            min_value += pairs[i]
            max_value += pairs[-i-1]
        return max_value - min_value

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort()

        while len(stones) >= 2:
            s1 = stones.pop()
            s2 = stones.pop()

            if s1 != s2:
                stones.append(abs(s1 - s2))
            
            stones.sort()
        
        return stones[0] if stones else 0
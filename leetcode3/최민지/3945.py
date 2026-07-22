from collections import Counter

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        c = Counter(str(n))
        result = 0
        for i in c:
            result += int(i) * c[i]
        
        return result
            
        
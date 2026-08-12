from collections import defaultdict
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = defaultdict(int)
        for d in deck:
            counter[d] += 1
        
        count = counter[deck[0]]
        for _, freq in counter.items():
            if freq == 1:
                return False
            count = gcd(count, freq)

        return True if count != 1 else False
    

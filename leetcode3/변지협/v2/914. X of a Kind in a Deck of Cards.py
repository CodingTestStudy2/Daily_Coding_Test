from collections import defaultdict
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False

        dic = defaultdict(int)
        for d in deck:
            dic[d] += 1

        n = len(deck)

        print(dic)
        
        ans = False
        for i in range(2,n//2+2):
            if all([j % i == 0 for j in dic.values()]):
                ans = True
                break

        return ans
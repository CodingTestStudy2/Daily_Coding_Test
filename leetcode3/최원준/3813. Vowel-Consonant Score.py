class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vc = [0,0]
        for c in s:
            if c in ('a','e','i','o','u'):
                vc[0]+=1
            elif c.isalpha():
                vc[1]+=1
        return floor(vc[0]/vc[1]) if vc[1]>0 else 0

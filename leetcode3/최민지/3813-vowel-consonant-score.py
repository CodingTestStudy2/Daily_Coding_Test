class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        A = ['a', 'e', 'i', 'o', 'u']
        v, c = 0, 0
        for i in s:
            if i in A:
                v += 1
            else:
                c +=1
        return floor(v / c)
        
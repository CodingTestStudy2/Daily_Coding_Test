from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        maxnum1 = 0
        maxnum2 = 0
        count = Counter(s)
        find = ['a', 'e', 'i', 'o', 'u']

        for i in set(s):
            if i in find:
                maxnum1 = max(maxnum1, count[i])
            else:
                maxnum2 = max(maxnum2, count[i])
        
        return maxnum1 + maxnum2

        

#

'''
1. 아이디어 :
dictionary를 사용해서 distinct를 유지한다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''
from collections import defaultdict
class Solution:
    def residuePrefixes(self, s: str) -> int:
        counter = defaultdict(int)
        distinct = 0
        ans = 0

        for i in range(len(s)):
            char = s[i]
            if counter[char] == 0:
                distinct +=1
            counter[char] +=1
            if (i+1) % 3 == distinct:
                ans+=1
        return ans    

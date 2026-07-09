#

'''
1. 아이디어 :
Counter를 사용한다

2. 시간복잡도 :
    O(26)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        
        max_v = 0
        max_c = 0

        for char, freq in c.items():
            if char in ("a","e","i","o","u"):
                max_v = max(max_v, freq)
            else:
                max_c = max(max_c, freq)
        return max_v + max_c

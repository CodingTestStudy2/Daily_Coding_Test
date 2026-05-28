'''
1. 아이디어 : 
    뒤집어서 거꾸로인거 같은지 체크 
2. 시간복잡도 :
    O(n)
3. 자료구조/알고리즘 :
'''
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        ans = 99999
        for i in range(n):
            if s[i] == s[::-1][i]:
                return i
        
        return -1
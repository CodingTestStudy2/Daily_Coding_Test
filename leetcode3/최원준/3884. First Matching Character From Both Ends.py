#

'''
1. 아이디어 :


2. 시간복잡도 :
    O()

3. 자료구조/알고리즘 :


'''
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        for i in range(n//2+1):
            if s[i] == s[n-i-1]:
                return i
        return -1

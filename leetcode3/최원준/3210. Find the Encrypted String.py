#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k = k%n
        ans = ""
        for i in range(n):
            ans+=s[(k+i)%n]
        return ans

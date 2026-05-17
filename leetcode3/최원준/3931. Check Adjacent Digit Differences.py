#

'''
1. 아이디어 :


2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :


'''

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        return False if any( abs(int(s[i]) - int(s[i+1])) > 2 for i in range(len(s)-1)) else True

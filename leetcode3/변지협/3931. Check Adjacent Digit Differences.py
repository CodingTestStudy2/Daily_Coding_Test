
'''
1. 아이디어 :
2. 시간복잡도 :
    O(n)
3. 자료구조/알고리즘 :
'''

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        lst = []
        for i in range(len(s) - 1):
            lst.append(abs(int(s[i]) - int(s[i+1])))

        # if len(lst) == 1:
        #     return True if lst[0] <= 2 else False

        return True if max(lst) <= 2 else False 
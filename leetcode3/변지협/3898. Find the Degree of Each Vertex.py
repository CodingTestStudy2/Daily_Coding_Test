

'''
1. 아이디어 :
2. 시간복잡도 :
    O(n^2)
3. 자료구조/알고리즘 :
'''

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        ans = [0] * n
        
        for m in matrix:
            for i in range(len(m)):
                ans[i] += m[i]

        return ans
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
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(m) for m in matrix]

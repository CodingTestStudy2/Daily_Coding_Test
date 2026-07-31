'''
1. 아이디어 :
2. 시간복잡도 :
3. 자료구조/알고리즘 :
'''

class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))
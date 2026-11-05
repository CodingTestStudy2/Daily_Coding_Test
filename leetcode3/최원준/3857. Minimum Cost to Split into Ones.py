#

'''
1. 아이디어 :
n을 n-1 + 1로 매번 계산하면 최소값이 됩니다

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def minCost(self, n: int) -> int:
        return n * (n-1) // 2

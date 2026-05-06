#

'''
1. 아이디어 :
n은 100,000 까지.
1부터 999까지는 0개, 그 외에는 1개 이므로, n - 999

2. 시간복잡도 :
    O(1)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n - 999)
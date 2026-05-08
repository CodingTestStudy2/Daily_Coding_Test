#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
'''
class Solution:
    def countCommas(self, n: int) -> int:
        _sum = 0
        for i in range(1,n+1):
            if i >= 1000:
                _sum += 1
        
        return _sum

            
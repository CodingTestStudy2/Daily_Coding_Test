#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(len(n))

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        string = str(n)
        n_sum = 0
        n_product = 1

        for c in string:
            n_int = int(c)
            n_sum += n_int
            n_product *= n_int
        
        return n%(n_sum+n_product) == 0

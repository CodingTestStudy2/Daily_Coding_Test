
'''
1. 아이디어 :
2. 시간복잡도 :
    O(n)
3. 자료구조/알고리즘 :
'''

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0: return n
        
        non_zero = str(n).replace('0', '')
        sum_val = sum([int(i) for i in non_zero])
        x = int(non_zero)

        return x * sum_val
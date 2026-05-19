'''
1. 아이디어 :
2. 시간복잡도 :
    O(n)
3. 자료구조/알고리즘 :
'''
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return True if str(x) in str(n) and str(x) != str(n)[0] else False
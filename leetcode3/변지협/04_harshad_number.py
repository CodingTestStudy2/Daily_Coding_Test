#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
'''
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        str_x = str(x)
        _sum = 0
        for i in str_x:
            _sum += int(i)
        
        # print(_sum)
        
        if x % _sum == 0:
            return _sum
        else:
            return -1 
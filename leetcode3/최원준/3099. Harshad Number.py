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
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = sum([int(char) for char in str(x)])
        return total if x % total == 0 else -1

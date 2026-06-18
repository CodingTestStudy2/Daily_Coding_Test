#

'''
1. 아이디어 :
- n이 위치한 구간을 찾는다. (예: 10~99, 1000~9999, ...)
- 해당 구간에서 몇번째 숫자인지 구한다.
- 몇번째 숫자인진 몰라도, 해당 숫자의 몇번째 인덱스인지 구한다.

2. 시간복잡도 :
    O(logn)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        9 - 0 = 9 * 1
        99 - 9 = 90 * 2
        999 - 99 = 900 * 3
        9999 - 999 = 9000 * 4
        99999 - 9999 = 90000 * 5
        """

        digits = 1
        min_value = 1
        max_value = 9

        while n > digits * max_value:
            n -= digits * max_value
            digits += 1
            min_value *= 10
            max_value *= 10
        
        # print(n)
        # print(digits, min_value, max_value)
        nth = (n-1) // digits + min_value
        index = (n-1) % digits

        return int(str(nth)[index])

'''
1. 아이디어:
이진탐색으로 풀이.
2. 시간복잡도:
o(log n)
3. 알고리즘:
이진탐색
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        current = n // 2 + 1

        # while True:
        while True:
            # print(current)
            g = guess(current)

            if g == -1:
                n = current
                current = n // 2
            elif g == 1:
                current = (n + current + 1) // 2
            else:
                return current

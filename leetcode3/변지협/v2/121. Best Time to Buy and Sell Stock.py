
'''
1. 아이디어 :
처음 가격부터 끝 가격까지 왼쪽에서 최소값, 오른쪽에서 최대값을 구한 후 최대값 - 최소값을 구한다.

2. 시간복잡도 :
o(n)

3. 자료구조/알고리즘 :
dp
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = []
        right = []
        n = len(prices)

        tmp = 99999
        for price in prices:
            if tmp > price:
                left.append(price)
                tmp = price
            else:
                left.append(tmp)

        tmp = -1
        for price in prices[::-1]:
            if tmp < price:
                right.append(price)
                tmp = price
            else:
                right.append(tmp)
        right = right[::-1]

        return max([right[i] - left[i] for i in range(n)])
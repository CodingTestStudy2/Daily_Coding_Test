'''
1. 아이디어 :
- 왼쪽에서부터 순회하며 "그 날까지의 최저가"를 minlst에 누적한다.
- 각 날의 price에서 그 날까지의 최저가를 빼면 "그 날 팔았을 때의 최대 이익"이 된다.
- 그 이익들 중 최댓값이 정답.

2. 시간복잡도 :
o(n)  (최저가 누적 1번 + 이익 계산 1번)

3. 자료구조/알고리즘 :
- 누적 최솟값(prefix min) / dp

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minlst = []
        _min = 10e9

        for price in prices:
            if _min > price:
                _min = price
            minlst.append(_min)

        ans = []
        for i, price in enumerate(prices):
            ans.append(price - minlst[i])

        return max(ans)

#

'''
1. 아이디어 :
선택할 수 있는 돌의 길이를 1부터 계산.
반복 계산을 하지 않기 위해 dp 사용.
l~r에서 가장 효율적으로 돌을 가져가는 방법은 l + (l+1 ~ r) 또는 (l~r-1) + r

2. 시간복잡도 :
    O(n + n * n)

3. 자료구조/알고리즘 :
dp

'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]
        

        for length in range(2, n+1):
            for lp in range(n - length + 1):
                rp = lp + length - 1

                left = piles[lp] - dp[lp+1][rp]
                right = piles[rp] - dp[lp][rp-1]
                dp[lp][rp] = max(left, right)

        return dp[0][n-1] > 0

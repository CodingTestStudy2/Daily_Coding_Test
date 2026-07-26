#

'''
1. 아이디어 :
s[left:right+1] 구간을 출력하는 최소 횟수
"aba"를 보면:
dp[0][2] = 1 + dp[1][2] = 3

s[0] == s[2]이므로
dp[0][2] = dp[1][1] + dp[2][2]
         = 1 + 1
         = 2

2. 시간복잡도 :
    O(n**2)

3. 자료구조/알고리즘 :
dp

'''

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        # dp[left][right]:
        # s[left:right + 1]을 출력하는 최소 횟수
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        # 짧은 구간부터 계산
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                # s[left]를 별도로 한 번 출력
                dp[left][right] = 1 + dp[left + 1][right]

                # s[left]와 같은 문자를 출력하는 턴에 같이 처리
                for k in range(left + 1, right + 1):
                    if s[left] == s[k]:
                        middle = dp[left + 1][k - 1] if left + 1 <= k - 1 else 0

                        dp[left][right] = min(
                            dp[left][right],
                            middle + dp[k][right]
                        )

        return dp[0][n - 1]

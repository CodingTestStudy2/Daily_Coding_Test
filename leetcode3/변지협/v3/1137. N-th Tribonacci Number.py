'''
1. 아이디어 :
점화식 T(n) = T(n-1) + T(n-2) + T(n-3) 을 그대로 DP로 옮긴다.
dp[0]=0, dp[1]=1, dp[2]=1 을 초기값으로 두고 n까지 채운 뒤 dp[n]을 반환.

2. 시간복잡도 :
o(n) - n까지 한 번만 순회

3. 자료구조/알고리즘 :
DP (1차원 배열), 점화식

'''

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * 40

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]

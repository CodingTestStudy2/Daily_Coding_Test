"""
1. 아이디어 :
- 피보나치 수열 미리 구해놓고, 3개의 연속된 피보나치 수의 합을 set에 미리 넣음
- 그 set에 n이 있는지 확인한다.

2. 시간복잡도 :
o(1) (피보나치 수열은 1000번째까지만 구하면 됨)

3. 자료구조/알고리즘 :
"""

class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        m = 1000
        dp = [0] * m
        dp[0] = 0
        dp[1] = 1

        for i in range(2,m):
            dp[i] = dp[i-1] + dp[i-2]
        
        st = set()
        for i in range(2,m):
            st.add(dp[i] + dp[i-1] + dp[i-2])
        
        return n in st
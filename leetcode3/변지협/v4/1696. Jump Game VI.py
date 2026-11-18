'''
실패 (시간초과)
o(n*k)

1. 아이디어 :
dp[i] = i에 도착했을 때의 최대 점수.
dp[i] = nums[i] + max(dp[i-1], ..., dp[i-k]) 로 점화식을 세우고,
앞의 k개를 매번 for문으로 훑어서 최댓값을 구했다.

2. 시간복잡도 :
o(n*k) — n=10^5, k=10^5 이면 10^10 이라 시간초과.
(슬라이딩 윈도우 최댓값 deque로 줄여야 함)

3. 자료구조/알고리즘 :
dp (1차원 배열), 완전탐색 max

'''

class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1,n):
            _max = -10e9
            for j in range(k):
                x = i-j-1
                if x >=0:
                    _max = max(_max,dp[i-j-1])

            dp[i] = nums[i] + _max 

        return dp[n-1]

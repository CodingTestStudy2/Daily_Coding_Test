class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 1. 양 끝에 가상 풍선 1 추가 및 길이 정의
        A = [1] + nums + [1]
        n = len(A)

        # 2차원 dp 테이블 초기화 (dp[i][j] 사이의 풍선들을 모두 터뜨렸을 떄의 최대 점수 )
        dp = [[0] * n for _ in range(n)]

        # 구간의 길이(length)를 2부터 n-1까지 늘려가며 계산
        for length in range(2, n):
            for left in range(0, n-length):
                right = left + length

                # left와 right의 사이에서 '가장 마지막으로 터뜨릴 풍선 k'를 탐색
                for k in range(left + 1, right):
                    coins = dp[left][k] + dp[k][right] + (A[left] * A[k] * A[right])
                
                    if coins > dp[left][right]:
                        dp[left][right] = coins

        return dp[0][n-1]
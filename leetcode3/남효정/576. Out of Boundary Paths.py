class Solution:

    # 풍선 k가 가장 마지막으로 터진다면 양 옆의 풍선은 무조건 l, r임
    # 그러므로 k 기준으로 좌측(left, k), 우측(k, right)로 나눠서 배열 작성함

    def maxCoins(self, nums: List[int]) -> int:
        # 양 끝 경계에 1을 추가한다
        A = [1] + nums + [1]
        n = len(A)
        dp = [[0] * n for _ in range(n)]

        # l과 r 사이의 거리 구하기 (2부터 n-1까지)
        for length in range(2, n):
            for l in range(n - length):
                r = l + length

                # l과 r 사이의 k 중 최댓값 찾아서 갱신함
                # k 마지막에 터뜨릴 때 얻는 코인 + 좌측 코인 + 우측 코인
                dp[l][r] = max(
                    A[l] * A[k] * A[r] + dp[l][k] + dp[k][r]
                    for k in range(l + 1, r)
                )

        return dp[0][n - 1]
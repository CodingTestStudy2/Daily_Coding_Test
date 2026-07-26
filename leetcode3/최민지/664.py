class Solution:
    def strangePrinter(self, s: str) -> int:

        @cache
        def dp(i, j):
            # 빈 문자열
            if i > j:
                return 0

            # 문자 하나
            if i == j:
                return 1

            # s[i]를 따로 출력하는 경우
            ans = dp(i + 1, j) + 1

            # s[i]와 같은 문자를 찾아 같이 출력
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    ans = min(ans,
                              dp(i + 1, k - 1) + dp(k, j))

            return ans

        return dp(0, len(s) - 1)
        
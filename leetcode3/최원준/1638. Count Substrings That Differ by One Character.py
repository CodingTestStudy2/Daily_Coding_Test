
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        same = [[0] * (m + 1) for _ in range(n + 1)]
        diff = [[0] * (m + 1) for _ in range(n + 1)]

        ans = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    same[i][j] = same[i - 1][j - 1] + 1
                    diff[i][j] = diff[i - 1][j - 1]
                else:
                    diff[i][j] = same[i - 1][j - 1] + 1

                ans += diff[i][j]

        return ans

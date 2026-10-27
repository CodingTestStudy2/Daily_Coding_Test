class Solution:
    def minRotations(self, s: str) -> int:
        ans = 0
        curr = 0

        for next in s:
            num = int(next)

            diff = abs(curr-num)
            ans += min(diff, 10-diff)
            curr = num
        return ans

class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        curr = 0
        ans = 0
        for r in requests:
            ans += abs(curr - r)
            curr = r
        return ans

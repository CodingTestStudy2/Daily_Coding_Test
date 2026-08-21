class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        now = 0
        result = 0
        for req in requests:
            result += abs(req - now)
            now = req
        return result
        
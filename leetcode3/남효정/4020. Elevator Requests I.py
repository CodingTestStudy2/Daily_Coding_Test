class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        ans = 0
        requests = [0] + requests
        for i in range(len(requests)-1):
            ans += abs(requests[i] - requests[i+1])
        return ans
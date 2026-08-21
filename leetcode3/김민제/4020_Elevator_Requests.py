class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total=0
        before=0
        for n in requests:
            total=total+(abs(n-before))
            before=n
        return total
n = 3
requests = [2,0,0]
solution = Solution()
print(solution.elevatorRequests(n, requests))

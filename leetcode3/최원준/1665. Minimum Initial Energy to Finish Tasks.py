class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        ans = 0
        curr = 0

        for actual, minimum in tasks:
            ans = max(ans, curr + minimum)
            curr += actual

        return ans

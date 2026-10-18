class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            height = heights[i]

            while stack and stack[-1] < height:
                stack.pop()
                answer[i] += 1

            if stack:
                answer[i] += 1

            stack.append(height)

        return answer

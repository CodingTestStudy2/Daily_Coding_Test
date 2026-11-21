class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        tasks.sort(reverse=True)

        n = len(tasks)
        ans = n
        sessions = []

        def backtrack(idx):
            nonlocal ans

            if len(sessions) >= ans:
                return

            if idx == n:
                ans = len(sessions)
                return

            for i in range(len(sessions)):
                if sessions[i] + tasks[idx] > sessionTime:
                    continue

                sessions[i] += tasks[idx]
                backtrack(idx + 1)
                sessions[i] -= tasks[idx]

            sessions.append(tasks[idx])
            backtrack(idx + 1)
            sessions.pop()

        backtrack(0)
        return ans

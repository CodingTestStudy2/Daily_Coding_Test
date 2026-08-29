class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        ans = [0] * n

        prev_time = 0

        for log in logs:
            id, se, time = log.split(":")
            id = int(id)
            time = int(time)

            if se == "start":
                if stack:
                    ans[stack[-1]] += time - prev_time

                stack.append(id)
                prev_time = time

            else:  # end
                ans[stack[-1]] += time - prev_time + 1
                stack.pop()
                prev_time = time + 1

        return ans

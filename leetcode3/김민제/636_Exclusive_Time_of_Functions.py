from typing import List

'''
문제 풀이 이해는 했지만
직접 풀지는 못했음.
'''

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        prev_time = 0

        for log in logs:
            temp = log.split(":")
            func_id = int(temp[0])
            action = temp[1]
            timestamp = int(temp[2])

            if action =="start":
                if stack:
                    result[stack[-1]] += timestamp-prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:
                result[stack.pop()] += timestamp - prev_time +1
                prev_time = timestamp+1
        return result

n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

solution = Solution()
print(solution.exclusiveTime(n,logs))

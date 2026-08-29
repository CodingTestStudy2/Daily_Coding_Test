# 풀이 실패
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_id_str, typ, timestamp_str = log.split(":")
            fn_id, curr_time = int(fn_id_str), int(timestamp_str)

            if typ == "start":
                # 이미 실행 중인게 있으면 실행시간 누적
                # 이전 함수가 prev_time ~ curr_time - 1까지 수행되었음
                if stack:
                    res[stack[-1]] += curr_time - prev_time

                stack.append(fn_id)
                prev_time = curr_time
            else:
                popped_id = stack.pop()
                res[popped_id] += curr_time - prev_time + 1

                # 타임스탬프 끝까지 차지하므로 다음 시작점은 +1임
                prev_time = curr_time + 1
        
        return res
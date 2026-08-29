class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            fn_id, event, timestamp = log.split(":")
            fn_id = int(fn_id)
            curr_time = int(timestamp)
            
            if event == "start":
                if stack:
                    res[stack[-1]] += curr_time - prev_time
                
                stack.append(fn_id)
                prev_time = curr_time
            else:  
                res[stack.pop()] += curr_time - prev_time + 1
                prev_time = curr_time + 1
                
        return res
        
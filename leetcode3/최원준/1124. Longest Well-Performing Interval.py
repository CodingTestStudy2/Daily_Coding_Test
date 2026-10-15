TLE

class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        n = len(hours)

        for i, hour in enumerate(hours):
            hours[i] = 1 if hour>=9 else -1
        
        prefix_sum = [0] * (n+1)
        
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + hours[i]
            
        print(prefix_sum[1:])
        ans = 0

        map = {}

        # for start in range(n):
        #     for end in range(start + 1, n+1):
        #         if prefix_sum[end] - prefix_sum[start] > 0:
        #             ans = max(ans, end - start)

        # for i, prefix in enumerate(prefix_sum):


        return ans
            

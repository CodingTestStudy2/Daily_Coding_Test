class Solution:
    def countMonobit(self, n: int) -> int:
        result = 1

        x = 1
        while x <= n:
            result += 1
            x = x * 2 + 1
        return result
        
       # 0  2^0 -1
       # 1  2^1 -1
       # 11 2^2 -1
       # 111 2^3 -1 
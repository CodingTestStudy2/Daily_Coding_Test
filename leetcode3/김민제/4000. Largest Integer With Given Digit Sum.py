class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s==0:
            return 0
        sum_max = 0
        return_val = -1
        for num in range(10**(n-1),10**n):
            temp_max=0
            for x in str(num):
                temp_max += int(x)
            if s == temp_max:
                sum_max = max(sum_max,temp_max)
                return_val = num
        return return_val

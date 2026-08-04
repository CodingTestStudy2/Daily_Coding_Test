class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0: 
            return 0

        if n * 9 < s:
            return -1
        
        div = s // 9
        mod = s % 9

        if mod == 0:
            return int('9' * div + (n - div) * '0')

        return int('9' * div + str(mod) + (n - div - 1) * '0')
            
        
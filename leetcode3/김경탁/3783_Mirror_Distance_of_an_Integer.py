class Solution:
    def mirrorDistance(self, n: int) -> int:

        str_n=str(n)
        re=str_n[::-1]
        
        return abs(n-int(re))
        

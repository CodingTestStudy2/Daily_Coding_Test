class Solution:
    def mirrorDistance(self, n: int) -> int:
        strn = str(n)
        return abs(int(strn[::-1]) - n)
class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse_text=str(n)[::-1]
        return abs(n-int(reverse_text))

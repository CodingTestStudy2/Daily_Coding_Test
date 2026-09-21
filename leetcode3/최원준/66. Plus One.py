class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(c) for c in str(int("".join(str(d) for d in digits)) + 1)]

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        result = []
        for n in nums:
            if result.count(n) < k:
                result.append(n)
        return result
        
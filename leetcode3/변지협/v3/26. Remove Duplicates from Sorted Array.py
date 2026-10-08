from collections import Counter
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c = Counter(nums)
        nums[:] = c.keys()
        print(nums)
        return len(nums)
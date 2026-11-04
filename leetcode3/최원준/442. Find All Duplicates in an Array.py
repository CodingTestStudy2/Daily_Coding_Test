class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        return [num for num, count in Counter(nums).items() if count == 2]

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        s_len = len(nums)
        x = sum(nums[-k:])
        y = sum(nums[:k])
        return abs(x - y)
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n

        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
            

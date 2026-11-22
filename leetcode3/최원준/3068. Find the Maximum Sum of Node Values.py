class Solution:
    def maximumValueSum(
        self, nums: list[int], k: int, edges: list[list[int]]
    ) -> int:
        total = sum(nums)
        positive_count = 0
        min_diff = float('inf')

        for num in nums:
            diff = (num ^ k) - num

            if diff > 0:
                total += diff
                positive_count += 1

            min_diff = min(min_diff, abs(diff))

        if positive_count % 2 == 1:
            total -= min_diff

        return total

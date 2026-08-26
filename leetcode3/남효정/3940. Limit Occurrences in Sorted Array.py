class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        num_type = sorted(list(set(nums)))
        ans = []
        for num in num_type:
            num_cnt = nums.count(num)
            if num_cnt > k:
                ans += ([num] * k)
            else:
                ans += ([num] * num_cnt)
        return ans
        
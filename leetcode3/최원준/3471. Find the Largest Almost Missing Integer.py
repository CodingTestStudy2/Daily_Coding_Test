from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter(nums)

        if k == n:
            return max(nums)

        if k == 1:
            ans = -1

            for num in nums:
                if counter[num] == 1:
                    ans = max(ans, num)

            return ans

        # 1 < k < n
        ans = -1

        if counter[nums[0]] == 1:
            ans = max(ans, nums[0])

        if counter[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans

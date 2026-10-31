class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            even = set()
            odd = set()

            for j in range(i, n):
                num = nums[j]

                if num % 2 == 0:
                    even.add(num)
                else:
                    odd.add(num)

                if len(even) == len(odd):
                    ans = max(ans, j - i + 1)

        return ans

class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        ans = 0
        left = 0
        right = 0
        n = len(nums)

        counter = defaultdict(int)
        total = 0

        for right in range(n):
            rnum = nums[right]
            while counter[rnum] == 1:
                lnum = nums[left]
                counter[lnum] -= 1
                total -= lnum
                left +=1
            counter[rnum] +=1
            total += rnum
            ans = max(ans, total)
        
        return ans

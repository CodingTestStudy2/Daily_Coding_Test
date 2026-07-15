#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prev = nums[i-k] if i-k >= 0 else -float('inf')
            next = nums[i+k] if i+k < n else -float('inf')
            curr = nums[i]

            if prev < curr > next:
                ans += curr

        return ans


'''
1. 아이디어 :
2. 시간복잡도 :
3. 자료구조/알고리즘 :
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_cnt = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1

            while zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
        
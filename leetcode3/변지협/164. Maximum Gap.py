'''
1. 아이디어 :
    완전탐색
2. 시간복잡도 :
    O(n log n)
3. 자료구조/알고리즘 :
'''

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)-1):
            diff = abs(nums[i] - nums[i+1])
            if ans < diff:
                ans = diff
        
        return ans
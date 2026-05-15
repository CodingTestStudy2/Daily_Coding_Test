
'''
1. 아이디어 :
    그냥 문제 조건대로 for문 넣으면됨
2. 시간복잡도 :
    O(n)
3. 자료구조/알고리즘 :
'''

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums) * 2
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[len(nums)-i-1]
        
        return ans

'''
1. 아이디어 :
middle 원소 구하고, 그 원소가 유일한지 확인한다.

2. 시간복잡도 :
    o(n)
3. 자료구조/알고리즘 :
'''


class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        middle = nums[n//2]
        return True if 1 == len([i for i in nums if i == middle]) else False
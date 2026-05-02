#

'''
1. 아이디어 :
- 완전 탐색

2. 시간복잡도 :
    O(n^2)

3. 자료구조/알고리즘 :

'''


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        # print(nums)
        _set = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                _3sum = nums[i] + nums[left] + nums[right]
                if _3sum < 0:
                    left += 1
                elif _3sum > 0:
                    right -= 1
                else:
                    _set.add(tuple(sorted([nums[i],nums[left],nums[right]])))
                    left += 1
        
        # print(_set)
        return [list(s) for s in _set]
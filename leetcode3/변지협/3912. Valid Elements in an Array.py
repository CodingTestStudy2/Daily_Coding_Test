
'''
1. 아이디어 :
    왼쪽 오른쪽 최대 구하고 비교
2. 시간복잡도 :
    O(n^2)
3. 자료구조/알고리즘 :
'''
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        
        _max = 0
        for i in range(len(nums)):
            _max = max(nums[i], _max)
            left[i] = _max
        
        _max = 0
        for i in range(len(nums)-1, -1, -1):
            _max = max(nums[i], _max)
            right[i] = _max
        
        print(left, right)

        ans = []
        for i in range(len(nums)-1):
            if i == 0:
                ans.append(nums[i])
                continue
            
            # if i != 0 and i == len(nums) - 1:
            #     ans.append(nums[i])
            
            if max(left[:i]) < nums[i] or max(right[i+1:]) < nums[i]:
                ans.append(nums[i])
        
        # if len(nums) != 1:
        ans.append(nums[len(nums)-1])
        return ans
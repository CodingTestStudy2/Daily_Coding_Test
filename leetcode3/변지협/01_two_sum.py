'''
1. 아이디어 :
- 완전 탐색

2. 시간복잡도 :
    O(n^2)

3. 자료구조/알고리즘 :

'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                sum = nums[i]
                sum += nums[i+j+1]
                if sum == target:
                    return [i,i+j+1]
            
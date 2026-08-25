#

'''
1. 아이디어 :


2. 시간복잡도 :
    O(n + n)

3. 자료구조/알고리즘 :


'''
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum([nums[i] if i%2==0 else -nums[i] for i in range(len(nums))])

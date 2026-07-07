#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n-2)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-2):
            if (nums[i] + nums[i+2]) * 2== nums[i+1]:
                ans+=1
        return ans

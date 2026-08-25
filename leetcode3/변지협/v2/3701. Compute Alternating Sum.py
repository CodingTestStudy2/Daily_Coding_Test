'''
1. 아이디어 :
그냥 홀짝 더함

2. 시간복잡도 :
O(n)

3. 자료구조/알고리즘 :
'''
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if i % 2 == 0:
                ans += nums[i]
            else:
                ans -= nums[i]
        
        return ans
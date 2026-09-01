'''
1. 아이디어 :
문제에 명시되어있는 것 그대로 구현한다.

2. 시간복잡도 :
o(n^2)

3. 자료구조/알고리즘 :
'''
class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-1):
            _sum = 0
            _len = n - i - 1
            print(i, _len)
            for j in range(i+1,n):
                _sum += nums[j]
            
            avg = _sum / _len
            
            if avg < nums[i]:
                ans +=1
        
        return ans
#

'''
1. 아이디어 :
nums를 순회하면서 1과 2를 마주칠때마다 
- 1 또는 2의 마지막 인덱스와의 거리를 계산합니다.
- 인덱스를 저장합니다.


2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :


'''
class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        index1 = float('inf')
        index2 = float('inf')
        ans = float('inf')
        
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num == 1:
                ans = min(ans, abs(i-index2))
                index1 = i
            elif num == 2:
                ans = min(ans, abs(i-index1))
                index2 = i
        return -1 if ans == float('inf') else ans

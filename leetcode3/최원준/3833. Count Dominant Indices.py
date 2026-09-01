#

'''
1. 아이디어 :
총합을 구하고 인덱스를 옮겨가며 차감 후 계산

2. 시간복잡도 :
    O(n + n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        count = n

        ans = 0
        for i in range(n-1):
            total -= nums[i]
            count -= 1
            ans = ans + 1 if nums[i] > total/count else ans
        return ans

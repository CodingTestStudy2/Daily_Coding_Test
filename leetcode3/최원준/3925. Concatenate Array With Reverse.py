#

'''
1. 아이디어 :


2. 시간복잡도 :
    O()

3. 자료구조/알고리즘 :


'''


class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(nums[i])
        for i in range(n-1,-1,-1):
            ans.append(nums[i])
        return ans
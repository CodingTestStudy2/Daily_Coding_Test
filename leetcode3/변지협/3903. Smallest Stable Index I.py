
'''
1. 아이디어 :
2. 시간복잡도 :
    O(n^2)
3. 자료구조/알고리즘 :
'''

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_max_diff = []
        for i in range(len(nums)):
            min_max_diff.append(max(nums[:i+1]) - min(nums[i:]))
        
        print(min_max_diff)

        for i in range(len(nums)):
            if min_max_diff[i] <= k:
                return i

        return -1
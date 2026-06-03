#

'''
1. 아이디어 :


2. 시간복잡도 :
    O(n**2)

3. 자료구조/알고리즘 :


'''

from collections import Counter
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        nums.sort()

        for x in nums:
            for y in nums:
                if x == y or x >= y:
                    continue
                if counter.get(x) == counter.get(y):
                    continue
                return [x, y]

        return [-1, -1]
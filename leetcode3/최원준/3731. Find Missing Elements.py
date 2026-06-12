#

'''
1. 아이디어 :
최소, 최대를 구한후 최소~최대 순회하며 없는것들을 리스트에 추가.

2. 시간복잡도 :
    O(n + n + n)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        cmin = float('inf')
        cmax = -float('inf')
        for num in nums:
            cmin = min(cmin, num)
            cmax = max(cmax, num)

        ans = []
        for num in range(cmin, cmax):
            if num not in nums_set:
                ans.append(num)
        
        return ans


'''
1. 아이디어 :
2. 시간복잡도 :
    o(n * m)

3. 자료구조/알고리즘 :
'''
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []
        
        for i in nums:
            if len([j for j in ans if j == i]) == k:
                continue
            ans.append(i)
        
        return ans
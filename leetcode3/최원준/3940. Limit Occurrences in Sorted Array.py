from collections import defaultdict
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        counter = defaultdict(int)
        ans = []
        for num in nums:
            if counter[num] == k:
                continue
            counter[num]+=1
            ans.append(num)
        
        return ans

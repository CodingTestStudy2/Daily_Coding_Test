class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        result = []
        for i in nums:
            count = 0
            for j in range(len(nums)-k+1):
                sub = nums[j:j+k]
                if i in sub:
                    count += 1
            if count == 1:
                result.append(i)
            result.sort()
        if result: 
            return result[-1]
        return -1

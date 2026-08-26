class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        new_array=[]
        for n in nums:
            if new_array.count(n)<k:
                new_array.append(n)
        return new_array

nums = [1,1,1,2,2,3]
k = 2
solution = Solution()
print(solution.limitOccurrences(nums,k))

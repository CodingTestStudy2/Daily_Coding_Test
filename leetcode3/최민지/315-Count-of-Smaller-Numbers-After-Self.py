class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            temp = 0
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    temp += 1
            result.append(temp)

        return result

        
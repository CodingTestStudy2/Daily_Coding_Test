class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        return [num for num, count in Counter(nums).items() if count == 2]



class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                result.append(abs(num))
            else:
                nums[idx] *= -1

        return result

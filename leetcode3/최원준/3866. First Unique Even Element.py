class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        c = Counter(nums)
        for num, freq in c.items():
            if num%2==0 and freq == 1:
                return num
        return -1

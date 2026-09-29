class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        majority = n/2

        counter = Counter(nums)
        for num, freq in counter.items():
            if freq >= majority:
                return num
        
        return -1

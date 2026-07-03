class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        s = set(nums)

        avg = max(1, sum(nums) // len(nums) + 1 )
        
        while avg in s:
            avg += 1
        
        return avg
        

        
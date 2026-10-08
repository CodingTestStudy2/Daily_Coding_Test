class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0
        visited = set()
        n = len(nums)
        count = 0
        for i in range(n):
            num = nums[i]
            if num in visited:
                continue
            
            visited.add(num)
            nums[index] = num
            index+=1
            count+=1
        
        return count
        

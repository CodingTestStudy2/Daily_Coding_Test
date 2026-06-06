'''
input: array
output: index of the target element (equal possibility)

preprocess
- go through the array and make the dictionary



TC: O(N) - preprocess, O(1) - pick
SC: O(N)
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(len(nums)):
            if nums[i] not in self.dict:
                self.dict[nums[i]] = []
            self.dict[nums[i]].append(i)
 
        

    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
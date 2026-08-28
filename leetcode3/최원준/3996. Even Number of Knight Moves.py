class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (abs(start[0] - target[0]) + abs(start[1] - target[1])) % 2 ==0

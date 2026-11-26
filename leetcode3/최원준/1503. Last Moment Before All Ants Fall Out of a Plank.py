class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        '''
        left = [3, 4] right = [0, 1]
        left = [2, 3] right = [1, 2]
        '''

        left.sort()
        right.sort()
        return max(left[-1] if left else 0, n-right[0] if right else 0)
        

        

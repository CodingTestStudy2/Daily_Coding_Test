class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:

        result = []

        for i in matrix:
            temp = 0
            for j in i:
                if j == 1:
                    temp += 1
            result.append(temp)
    
        return result
        
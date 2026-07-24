class Solution:
    def createGrid(self, n: int, m: int) -> list[str]:
        ans = []
        for row in range(n):
            temp = ""
            for col in range(m):
                if row == n-1 or col == 0:
                    temp += "."
                else:
                    temp += "#"
            ans.append(temp)
        
        return ans

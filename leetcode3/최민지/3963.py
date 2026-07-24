class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [] 
        # 종료 지점 (m-1, n-1)
        grid.append('.' * n)
        for i in range(m-1):
            grid.append('#' * (n-1) + '.')
        return grid
        
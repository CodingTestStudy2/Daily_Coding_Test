class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        def is_valid(x, y, size):
            target = sum(grid[x][y:y+size])

            for i in range(x, x+size):
                total = 0
                for j in range(y, y+size):
                    total += grid[i][j]
                if total != target:
                    return False

            for i in range(y, y+size):
                total = 0
                for j in range(x, x+size):
                    total += grid[j][i]
                if total != target:
                    return False

            diag_pos = 0
            diag_neg = 0

            for i in range(size):
                diag_pos += grid[x+i][y+i]
                diag_neg += grid[x+i][y+size-1-i]

            return diag_pos == target and diag_neg == target

        n = len(grid)
        m = len(grid[0])
        max_size = 1

        for row in range(n):
            for col in range(m):
                max_distance = min(n-row, m-col)

                for distance in range(max_size+1, max_distance+1):
                    if is_valid(row, col, distance):
                        max_size = distance

        return max_size

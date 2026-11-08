class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        answer = []

        for start in range(n):
            col = start

            for row in range(m):
                next_col = col + grid[row][col]

                # 벽에 부딪히는 경우
                if next_col < 0 or next_col >= n:
                    col = -1
                    break

                # V자 형태로 막히는 경우
                if grid[row][col] != grid[row][next_col]:
                    col = -1
                    break

                # 다음 열로 이동
                col = next_col

            answer.append(col)

        return answer

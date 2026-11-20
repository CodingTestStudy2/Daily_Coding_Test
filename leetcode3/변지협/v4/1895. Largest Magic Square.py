'''
1. 아이디어 :
부분 정사각형 크기를 큰 것(min(n,m))부터 1씩 줄여가며 완전탐색.
각 후보 정사각형의 모든 행 합 / 열 합 / 두 대각선 합을 set에 넣고
set 크기가 1이면 마방진 → 그 크기가 정답.

2. 시간복잡도 :
o(min(n,m) * n * m * k^2) (k = 후보 크기, 각 후보마다 k^2 합 계산)

3. 자료구조/알고리즘 :
완전탐색(브루트포스), set

'''

class Solution:
    def is_magic(self, lst) -> bool:
        n = len(lst)

        st = set()
        for y in range(n):
            xsum = 0
            ysum = 0
            for x in range(n):
                xsum += lst[y][x]
                ysum += lst[x][y]
            st.add(xsum)
            st.add(ysum)

        case1 = [(i, i) for i in range(n)]
        case2 = [(n-i-1, i) for i in range(n)]

        st.add(sum([lst[y][x] for x, y in case1]))
        st.add(sum([lst[y][x] for x, y in case2]))

        if len(st) == 1:
            return True
        return False

    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        m = len(grid)

        for ans in range(min(n, m), 1, -1):
            for y in range(m-ans+1):
                for x in range(n-ans+1):
                    if self.is_magic([row[x:x+ans] for row in grid[y:y+ans]]):
                        return ans

        return 1

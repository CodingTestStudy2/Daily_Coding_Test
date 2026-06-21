#

'''
1. 아이디어 :
각 grid에 2가지 정보를 저장한다. 지금까지 온 경로의:
- 현재 체력이 제일 높은 경로의 [현재 체력, 최악의 체력]
- 지금까지 가장 덜 위험했던 경로의 [현재 체력, 최악의 체력]

매 grid를 방문할때마다 왼쪽의 ([현재 체력, 최악의 체력], [현재 체력, 최악의 체력])과 위의 ([현재 체력, 최악의 체력], [현재 체력, 최악의 체력])을 대상으로 계산한다.

2. 시간복잡도 :
    O(n*m*2)

3. 자료구조/알고리즘 :
누적합

'''

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])

        grids = [[None for _ in range(m)] for _ in range(n)]

        initial = dungeon[0][0]
        grids[0][0] = ([initial, initial], [initial, initial])

        def update(path, value):
            cur, worst = path
            new_cur = cur + value
            new_worst = min(worst, new_cur)
            return [new_cur, new_worst]

        def select(paths):
            best_current = max(paths, key=lambda x: (x[0], x[1]))
            best_worst = max(paths, key=lambda x: (x[1], x[0]))
            return best_current, best_worst

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue

                candidates = []
                value = dungeon[i][j]

                if i > 0:
                    up_current, up_worst = grids[i - 1][j]
                    candidates.append(update(up_current, value))
                    candidates.append(update(up_worst, value))

                if j > 0:
                    left_current, left_worst = grids[i][j - 1]
                    candidates.append(update(left_current, value))
                    candidates.append(update(left_worst, value))

                grids[i][j] = select(candidates)

        end_current, end_worst = grids[n - 1][m - 1]

        return min(
            max(1, 1 - end_current[1]),
            max(1, 1 - end_worst[1])
        )

from collections import defaultdict, Counter

class DetectSquares:

    def __init__(self):
        self.x_axis = defaultdict(list)
        self.y_axis = defaultdict(Counter)

    def add(self, point: list[int]) -> None:
        x, y = point

        self.x_axis[x].append(y)
        self.y_axis[y][x] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        ans = 0

        for ny in self.x_axis[x]:
            if ny == y:
                continue

            distance = abs(ny - y)

            for nx in (x + distance, x - distance):
                ans += (self.y_axis[y][nx]* self.y_axis[ny][nx])

        return ans

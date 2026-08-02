class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        rows = len(isInfected)
        cols = len(isInfected[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        total_walls = 0

        while True:
            visited = [[False] * cols for _ in range(rows)]

            regions = []
            threatened_cells = []
            walls_needed = []

            for row in range(rows):
                for col in range(cols):
                    if isInfected[row][col] != 1 or visited[row][col]:
                        continue

                    region = []
                    threatened = set()
                    wall_count = 0

                    stack = [(row, col)]
                    visited[row][col] = True

                    while stack:
                        current_row, current_col = stack.pop()
                        region.append((current_row, current_col))

                        for dr, dc in directions:
                            next_row = current_row + dr
                            next_col = current_col + dc

                            if not (
                                0 <= next_row < rows
                                and 0 <= next_col < cols
                            ):
                                continue

                            if isInfected[next_row][next_col] == 1:
                                if not visited[next_row][next_col]:
                                    visited[next_row][next_col] = True
                                    stack.append((next_row, next_col))

                            elif isInfected[next_row][next_col] == 0:
                                threatened.add((next_row, next_col))
                                wall_count += 1

                    regions.append(region)
                    threatened_cells.append(threatened)
                    walls_needed.append(wall_count)

            if not regions:
                break

            quarantine_index = 0

            for index in range(1, len(regions)):
                if (
                    len(threatened_cells[index])
                    > len(threatened_cells[quarantine_index])
                ):
                    quarantine_index = index

            if len(threatened_cells[quarantine_index]) == 0:
                break

            total_walls += walls_needed[quarantine_index]

            # 격리한 영역은 -1로 표시한다.
            for row, col in regions[quarantine_index]:
                isInfected[row][col] = -1

            # 나머지 영역은 인접한 0으로 전파된다.
            for index in range(len(regions)):
                if index == quarantine_index:
                    continue

                for row, col in threatened_cells[index]:
                    isInfected[row][col] = 1

        return total_walls

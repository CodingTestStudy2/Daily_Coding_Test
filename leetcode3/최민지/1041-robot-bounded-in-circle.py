class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0

        # 북, 동, 남, 서
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        direction = 0 

        for instruction in instructions:
            if instruction == 'G':
                dx, dy = directions[direction]
                x += dx
                y += dy

            elif instruction == 'R':
                direction = (direction + 1) % 4

            elif instruction == 'L':
                direction = (direction - 1) % 4

        return (x == 0 and y == 0) or direction != 0
        
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]

        instructions *= 4

        cords = [0, 0]
        dir = 0

        for ins in instructions:
            if ins == "G":
                cords[0] += dirs[dir][0]
                cords[1] += dirs[dir][1]

            elif ins == "R":
                dir = (dir + 1) % 4

            elif ins == "L":
                dir = (dir - 1) % 4

        return cords == [0, 0]

# 풀이 실패
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 동, 서, 남, 북
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # 좌표
        x, y = 0, 0

        # (북(0), 동(1), 남(2), 서(3))
        d = 0 

        # dir 배열에서 방향 변경될 때마다 인덱스 하나씩 이동
        for i in instructions:
            if i == "G":
                x += dirs[d][0]
                y += dirs[d][1]

            # 반시계 방향 회전
            elif i == "L":
                d = (d - 1) % 4

            # 시계 방향 회전
            elif i == "R":
                d = (d + 1) % 4
        
        # 원점으로 돌아오거나 북쪽을 바라보지 않으면 성공
        return (x == 0 and y == 0) or d != 0


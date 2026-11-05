#

'''
1. 아이디어 :
- 돌을 오른쪽으로 미는 메서드
오른쪽으로 밀때는 장애물을 만나기전까지 돌을 센 후, 장애물을 만나거나 끝까지 가면 다시 뒤로 가며 돌로 채운다.

- 90도로 회전하는 메서드

2. 시간복잡도 :
    O(n * m * m)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])
        
        def push_right(box):
            for row in box:
                stones = 0
                for i in range(m):
                    cell = row[i]
                    if cell == "#":
                        stones += 1
                        row[i] = "."
                    elif cell == ".":
                        pass
                    elif cell == "*":
                        for j in range(i-1, i-1-stones,-1):
                            row[j] = "#"
                        stones = 0
                for i in range(m-1, m-1-stones, -1):
                    row[i] = "#"
            return box
        
        boxGrid_push = push_right(boxGrid)

        
        def rotate_90(box):
            boxGrid90 = [[[""] for _ in range(n)] for _ in range(m)]
            for i in range(n):
                for j in range(m):
                    boxGrid90[j][n-i-1] = box[i][j]
            return boxGrid90
        
        return rotate_90(boxGrid_push)

        """
        [["#",".","*","."]
        ["#","#","*","."]]
        [
        [[''], ['']], 
        [[''], ['']], 
        [[''], ['']], 
        [[''], ['']]
        ]
        """

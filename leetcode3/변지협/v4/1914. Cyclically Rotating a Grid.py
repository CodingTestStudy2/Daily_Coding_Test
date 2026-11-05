'''
시간 초과
'''
'''
0,0 -> 0,1
0,1 -> 0,2
...
0,4 -> 0,5
0,5 -> 1,5
1,5 -> 2,5
2,5 -> 3,5
3,5 -> 3,4
'''
class Solution:
    def rotate_one(self, grid: List[List[int]]) -> List[List[int]]:
        xlen = len(grid[0])
        ylen = len(grid)
        vertexs = [(0,0),(0,ylen-1),(xlen-1,ylen-1),(xlen-1,0)]
        rotate_num = min(xlen,ylen) // 2
        tmp = [[0] * xlen for _ in range(ylen)]

        while rotate_num > 0:
            # print(rotate_num)
            # print(vertexs)

            for y in range(vertexs[0][1],vertexs[1][1]):
                tmp[y+1][vertexs[0][0]] = grid[y][vertexs[0][0]]
            
            # print(tmp)
            
            for x in range(vertexs[1][0],vertexs[2][0]):
                tmp[vertexs[1][1]][x+1] = grid[vertexs[1][1]][x]

            # print(tmp)
            
            for y in range(vertexs[2][1],vertexs[3][1],-1):
                tmp[y-1][vertexs[2][0]] = grid[y][vertexs[2][0]]

            # print(tmp)
            
            for x in range(vertexs[3][0],vertexs[0][0],-1):
                tmp[vertexs[3][1]][x-1] = grid[vertexs[3][1]][x]
            
            tmp2 = [
                (vertexs[0][0]+1,vertexs[0][1]+1),
                (vertexs[1][0]+1,vertexs[1][1]-1),
                (vertexs[2][0]-1,vertexs[2][1]-1),
                (vertexs[3][0]-1,vertexs[3][1]+1)
                ]
            vertexs = tmp2
            rotate_num -= 1
        return tmp

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        tmp = grid

        xlen = len(grid[0])
        ylen = len(grid)
        
        while k > 0:
            tmp = self.rotate_one(tmp)
            k-=1
        return tmp
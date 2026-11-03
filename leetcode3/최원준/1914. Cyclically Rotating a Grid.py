#

'''
1. 아이디어 :
가장 바깥쪽 layer부터 [0,0], [1,1], ...[n,n]원소를 가장 처음으로 원을 그리며 숫자와 위치를 각 배열에 저장.
배열에 저장된 숫자의 offset을 계산해서 offset이 위치하는 곳부터 가장 처음 원을 시작한 곳부터 채운다.

2. 시간복잡도 :
    O( min(n, m)/2 * n * m * 2)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        max_layer = min(n//2, m//2)
        layers = {}

        dx = [0,1,0,-1]
        dy = [1,0,-1,0]

        for layer in range(max_layer):
            pos =[]
            nums = []
            
            x, y = layer, layer
            direction = 0

            top = layer
            left = layer
            bottom = n - layer - 1
            right = m - layer - 1

            length = 2 * (bottom - top + right - left)

            for _ in range(length):
                pos.append((x, y))
                nums.append(grid[x][y])

                nx = x + dx[direction]
                ny = y + dy[direction]

                if not (top <= nx <= bottom and left <= ny <= right):
                    direction = (direction + 1 ) % 4
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                
                x, y = nx, ny
            
            offset = k % length
            nums = nums[offset:] + nums[:offset]

            for i in range(len(pos)):
                x, y = pos[i]
                grid[x][y] = nums[i]

        return grid




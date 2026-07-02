#

'''
1. 아이디어 :
범위의 위쪽 row, 아래쪽 row의 인덱스를 찾아서 바꿔줍니다.

2. 시간복잡도 :
    O(n*n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for row in range(x, x+k//2):
            for col in range(y, y+k):
                grid[row][col], grid[2 * x + k - 1 - row][col] = grid[2 * x + k - 1 - row][col], grid[row][col]
        return grid
        

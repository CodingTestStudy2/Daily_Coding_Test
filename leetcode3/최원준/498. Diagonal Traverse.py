#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n * m)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n = len(mat)
        m = len(mat[0])

        def get_next(x: int, y: int, going_up: bool):
            if going_up:
                if x == 0:
                    if y == m - 1:
                        return [x + 1, y]
                    else:
                        return [x, y + 1]
                elif y == m - 1:
                    return [x + 1, y]
                else:
                    return [x - 1, y + 1]

            else: 
                if y == 0:
                    if x == n - 1:
                        return [x, y + 1]
                    else:
                        return [x + 1, y]
                elif x == n - 1:
                    return [x, y + 1]
                else:
                    return [x + 1, y - 1]

        x = y = 0
        going_up = True

        for _ in range(n * m):
            ans.append(mat[x][y])
            nx, ny = get_next(x, y, going_up)

            if nx != x - 1 and nx != x + 1:
                going_up = not going_up
            elif ny != y - 1 and ny != y + 1:
                going_up = not going_up

            x, y = nx, ny

        return ans

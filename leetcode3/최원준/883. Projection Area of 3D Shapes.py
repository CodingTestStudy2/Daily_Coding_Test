#

'''
1. 아이디어 :
xy는 1 이상의 grid[i][j]
xz는 각 row의 최대값의 합
yz는 각 col의 최대값의 

2. 시간복잡도 :
    O(n * n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)

        """
        [ [1,2,3], [4,5,6], [7,8,9] ]
        """

        ans = 0
        for i in range(n):
            xz_max = 0
            yz_max = 0
            for j in range(n):
                ans += 1 if grid[i][j] != 0 else 0 # xy
                xz_max = max(xz_max, grid[i][j]) # xz
                yz_max = max(yz_max, grid[j][i]) # yz
            ans+=yz_max
            ans+=xz_max
                
        return ans


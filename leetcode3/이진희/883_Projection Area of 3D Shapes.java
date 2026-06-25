/* 

1. 아이디어 : 쌓여있는 블록의 3면의 합 구하기
              바닥은 블록 1개 이상 , row, col 기준 최댓값을을 각각 구해서 더해준다.

2. 시간복잡도 : O(N*M)*2

3. 자료구조/알고리즘 : 완전탐색

 */
class Solution {
    public int projectionArea(int[][] grid) {
        // 쌓여있는 모양
        // 가장자리 
        // 중간

        int ans = 0;
        for(int i=0; i<grid.length; i++) {
            int maxCol = 0;
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j]>=1) ans++;
                maxCol = Math.max(maxCol, grid[i][j]);
            }
            ans+=maxCol;
        }

        for(int i=0; i<grid[0].length; i++) {
            int maxRow = 0;
            for(int j=0; j<grid.length; j++) {
                maxRow = Math.max(maxRow, grid[j][i]);
            }
            ans+=maxRow;
        }

        return ans;  
    }
}
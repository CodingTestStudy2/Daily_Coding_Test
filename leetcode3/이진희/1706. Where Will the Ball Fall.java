/*

1. 아이디어 : 각 row마다 뱡향(1,-1)을 판단하여 움직임 갱심
             col기준 화살표 방향에 따라 좌하단이면 col-1이, 우하단이면 col+1이 같은 방향이어야 이동 가능
             for문으로 row = 1 부터 n-1까지 이동하며 이동 가능한지 체크
             각 방향에대한 조건을 나눠야한다

2. 시간복잡도 : O(N*M)

3. 자료구조/알고리즘 : 시뮬레이션

*/

class Solution {
    // 우 하단 방향 1
    // 좌 하단 방향 -1

    public int[] findBall(int[][] grid) {
        if(grid[0].length == 1) return new int[] {-1};

        int[] ans = new int[grid[0].length];
        Arrays.fill(ans, -1);

        for(int i=0; i<grid[0].length; i++) {
            ans[i] = canReach(i, grid);
        }

        return ans;
    }

    private int canReach(int idx, int[][] grid) {

        for(int i=0; i<grid.length; i++) {
           int dir = grid[i][idx];

           if(dir == 1) {
                if(idx+1 >= grid[0].length) return -1;
                if(grid[i][idx+1] == -1) return -1;
                idx++;
           }
           else {
                if(idx-1 < 0) return -1;
                if(grid[i][idx-1] == 1) return -1;
                idx--;
           }
        }

        return idx;
    }
}
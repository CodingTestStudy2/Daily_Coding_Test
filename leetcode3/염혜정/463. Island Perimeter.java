// 인접한 1의 개수를 구한다.
// 1 -> 3, 2 -> 2, 3 -> 1, 4 -> 0

class Solution {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public int islandPerimeter(int[][] grid) {
        int sum = 0;
        for (int i = 0; i<grid.length; i++) {
            for (int k = 0; k<grid[0].length; k++) {
                if (grid[i][k] == 0) continue;
                int cnt = adjacentCnt(grid, i, k);
                sum += calAdjacent(cnt);
            }
        }
        return sum;
    }

    int adjacentCnt (int[][] grid, int x, int y) {
        int cnt = 0;

        for (int i = 0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= grid.length || ny >= grid[0].length) continue;
            if (grid[nx][ny] == 1) cnt++;
        }
        return cnt;
    }

    int calAdjacent(int num) {
        switch (num) {
            case 0:
                return 4;
            case 1:
                return 3;
            case 2:
                return 2;
            case 3:
                return 1;
            default:
                return 0;
            }
    }
}

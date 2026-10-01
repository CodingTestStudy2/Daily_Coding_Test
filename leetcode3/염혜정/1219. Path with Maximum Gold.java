// dfs + 백트래킹

class Solution {
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    
    public int getMaximumGold(int[][] grid) {
        int max = 0;
        for (int i = 0; i<grid.length; i++) {
            for (int k = 0; k<grid[0].length; k++) {
                if (grid[i][k] == 0) continue;
                max = Math.max(max, dfs(grid, i, k));
            }
        }
        return max;
    }

    int dfs(int[][] grid, int x, int y) {
        if (x<0 || y<0 || x>=grid.length || y>=grid[0].length 
            || grid[x][y] == 0) return 0;

        int temp = grid[x][y];
        grid[x][y] = 0;

        int max = 0;
        for (int i = 0; i<4; i++) {
            max = Math.max(max, dfs(grid, x+dx[i], y+dy[i]));
        }
        grid[x][y] = temp;

        return max + temp;
    }

}

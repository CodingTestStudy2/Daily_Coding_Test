// dfs

class Solution {

    boolean[][] isVisited;
    int[] dr = {-1, 1, 0, 0};
    int[] dc = {0, 0, -1, 1};

    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        isVisited = new boolean[grid.length][grid[0].length];

        List<int[]> borders = new ArrayList<>();
        dfs (grid, row, col, grid[row][col], borders);

        for (int[] b : borders) {
            grid[b[0]][b[1]] = color;
        }

        return grid;
    }

    void dfs(int[][] grid, int row, int col, int gridColor, List<int[]> borders) {
        isVisited[row][col] = true;

        boolean isBorder = false;
        for (int i = 0; i<4; i++) {
            int nr = row + dr[i];
            int nc = col + dc[i];

            if (nr<0 || nr>=grid.length || nc<0 || nc>=grid[0].length) { // 테두리
                isBorder = true;
                continue;
            }

            if (grid[nr][nc] != gridColor) {
                isBorder = true;
                continue;
            }

            if (!isVisited[nr][nc]) {
                dfs(grid, nr, nc, gridColor, borders);
            }
        }
        if (isBorder) borders.add(new int[]{row, col});
    }
}

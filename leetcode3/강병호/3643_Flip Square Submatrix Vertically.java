class Solution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {
        // vertically revsering
        int cnt = k / 2;
        for (int i = x; i < x + cnt; i++) {

            // swap index
            // i - x : swap 횟수 
            int si = x + k - 1 - (i-x); 

            for (int j = y; j < y + k; j++) {
                int temp = grid[i][j];
                grid[i][j] = grid[si][j];
                grid[si][j] = temp;
            }
        }

        return grid;
    }
}
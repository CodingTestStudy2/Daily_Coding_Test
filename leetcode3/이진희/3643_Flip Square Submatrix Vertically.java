/*

1. 아이디어 : (x,y)를 왼쪽 위 좌표로 하는 k*k영역의 정사각형의 원소를 뒤집는다. 
              swap메소드를 구현하면 된다. 

2. 시간복잡도 : O(k*k)

3. 자료구조/알고리즘 : 구현

 */

class Solution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {
        // 뒤집기

        for(int i=0; i<k/2; i++) {
            int top = x+i;
            int bottom = x+k-i-1;

            for(int j=y; j<y+k; j++) {
                swap(grid, j, top, bottom);
            }
        }

        return grid;
    }

    private void swap(int[][] grid, int j, int top, int bottom) {
        int tmp = grid[top][j];
        grid[top][j] = grid[bottom][j];
        grid[bottom][j] = tmp;
    }
}
/* 

1. 아이디어 : 2차원 격자배열에서 raw,col좌표를 기준으로 같은색으로 연결된 칸을 전부 color로 바꾼다. 이때 경계값만 색칠해야 한다.

2. 시간복잡도 : O(N*M)

3. 자료구조/알고리즘 : bfs

 */

class Solution {
    private int[] dy = {0,1,0,-1};
    private int[] dx = {-1,0,1,0};
    private boolean[][] visited;
    private int n,m;

    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        
        n = grid.length;
        m = grid[0].length;
        visited = new boolean[n][m];

        return bfs(row, col, color, grid);
    }

    private int[][] bfs (int startY, int startX, int c, int[][] grid) {
        Deque<int[]> dq = new ArrayDeque<>();
        List<int[]> border = new ArrayList<>();

        dq.add(new int[]{startY, startX});
        visited[startY][startX] = true;
        int ori = grid[startY][startX];

        while(!dq.isEmpty()) {
            int[] curr = dq.poll();
            int y = curr[0];
            int x = curr[1];

            // 경계면만 바꾸기
            boolean check = false;

            for(int dir=0; dir<4; dir++) {
                int ny = y + dy[dir];
                int nx = x + dx[dir];

                if(ny<0 || ny>=n || nx<0 || nx>=m) {
                    check = true;
                    continue;
                }
                if(visited[ny][nx]) continue;
                if(grid[ny][nx] != ori) {
                    check = true;
                    continue;
                }

                dq.add(new int[]{ny, nx});
                visited[ny][nx] = true;
            }

            if(check) border.add(new int[]{y,x});
        }

        for(int[] b : border) {
            grid[b[0]][b[1]] = c;
        }

        return grid;
    }
}
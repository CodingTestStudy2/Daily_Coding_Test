/*
1. 아이디어:
   - 2차원 배열에서 가장 많은 금을 가지는 루트로 이동해서 최대 금의 합 구하기
   - 백트랙킹을 사용하기 때문에 dfs사용
   - 0이아닌 경로를 dfs로 돌리면서 최대 금의 개수를 누적한다.

2. 시간복잡도: O(N*M)

3. 자료구조/알고리즘: 백트랙킹
*/

class Solution {
    private boolean[][] visited;
    private int n,m;
    private int[] dy = {0,1,0,-1};
    private int[] dx = {1,0,-1,0};

    public int getMaximumGold(int[][] grid) {
        n = grid.length;
        m = grid[0].length;

        int gold = 0;

        visited = new boolean[n][m];

        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(grid[i][j] == 0 || visited[i][j]) continue;

                int currGold = dfs(grid,i,j);
                gold = Math.max(currGold, gold);
            }
        }

        return gold;
    }

    private int dfs(int[][] map, int y, int x) {

        int sum = 0;
        visited[y][x] = true;

        for(int dir=0; dir<4; dir++) {
            int ny = y + dy[dir];
            int nx = x + dx[dir];

            if(ny<0 || nx<0 || ny>=n || nx>=m) continue;
            if(visited[ny][nx] || map[ny][nx] == 0) continue;

            sum = Math.max(sum, dfs(map, ny, nx));
        }

        visited[y][x] = false;

        return sum + map[y][x];
    }
}
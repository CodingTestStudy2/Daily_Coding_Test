/*

1. 아이디어 : 인접행렬 그래프 탐색 문제
            grid2 격자 기준으로 섬을 탐색한다, 연결된 섬을 탐색하는 과정에서 grid1의 같은 위치에 하나라도 바다가 있다면, sub island를 만들 수 없으므로 false 반환
            전부 grid1 섬과 일치한다면, 포함 가능하다는 것이므로 true를 반환해준다

2. 시간복잡도 : O(N*M)

3. 자료구조/알고리즘 : bfs

 */

class Solution {
    private int lenY, lenX;
    private int[] dy = {0,1,0,-1};
    private int[] dx = {-1,0,1,0};
    private boolean[][] visited;

    // 0 = 바다
    // 1 = 섬
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        lenY = grid1.length;
        lenX = grid1[0].length;

        visited = new boolean[lenY][lenX];
        int ans = 0;

        for(int i=0; i<lenY; i++) {
            for(int j=0; j<lenX; j++) {
                if(visited[i][j] || grid2[i][j] == 0) continue;
                if(bfs(i,j,grid1,grid2)) ans++;
            }
        }

        return ans;
    }

    private boolean bfs(int startY, int startX, int[][] grid1, int[][] grid2) {
        Deque<int[]> dq = new ArrayDeque<>();
        boolean check = true;

        dq.add(new int[]{startY, startX});
        visited[startY][startX] = true;

        while(!dq.isEmpty()) {
            int[] curr = dq.poll();
            int y = curr[0];
            int x = curr[1];

            if(check && grid1[y][x] == 0) check = false;

            for(int dir=0; dir<4; dir++) {
                int ny = y + dy[dir];
                int nx = x + dx[dir];

                if(ny<0 || nx<0 || ny>=lenY || nx>=lenX) continue;
                if(visited[ny][nx] || grid2[ny][nx] == 0) continue;

                dq.add(new int[]{ny,nx});
                visited[ny][nx] = true;
            }
        }

        return check;
    }
}
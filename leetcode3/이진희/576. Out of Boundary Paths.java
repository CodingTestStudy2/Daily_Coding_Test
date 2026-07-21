/*

1. 아이디어 : 1~maxMove까지 움직였을때, 경계를 벗어나는 모든 경우의 수 구하기
              1차 시도: 메모제이션 없이 bfs로만 구현, 시간복잡도 O(4^maxMove)로 메모리 초과
              2차 시도: 메모제이션 적용, weight와 visited 배열을 추가하여 상태체크및 중복 방문 방지

2. 시간복잡도 : O(m*n*maxMove) 

3. 자료구조/알고리즘 : BFS, 메모제이션

 */

class Solution {
    
    private static int MOD = 1000000007;
    private int[] dy = {0,1,-1,0};
    private int[] dx = {1,0,0,-1};

    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        // 값이 너무 클 경우 10^9 + 7로 모듈러 연산

        Deque<int[]> dq = new ArrayDeque<>();
        dq.add(new int[]{startRow, startColumn, 0});

        long[][][] weight = new long[m][n][maxMove+1];
        boolean[][][] visited = new boolean[m][n][maxMove+1];
        long ans = 0L;

        weight[startRow][startColumn][0] = 1;
        visited[startRow][startColumn][0] = true;

        while(!dq.isEmpty()) {
            int[] curr = dq.poll();
            int y = curr[0];
            int x = curr[1];
            int moves = curr[2];
            long currWeight = weight[y][x][moves];

            if(moves == maxMove) continue;

            for(int dir=0; dir<4; dir++) {
                int ny = y + dy[dir];
                int nx = x + dx[dir];

                if(ny < 0 || nx < 0 || ny >= m || nx >=n ) ans=(ans+currWeight)%MOD;
                else {
                    weight[ny][nx][moves+1] = (weight[ny][nx][moves+1] + currWeight)%MOD;

                    if(!visited[ny][nx][moves+1]) {
                        visited[ny][nx][moves+1] = true;
                        dq.add(new int[]{ny,nx,moves+1});
                    }
                }
            }
        }

        return (int)ans;
    }
}
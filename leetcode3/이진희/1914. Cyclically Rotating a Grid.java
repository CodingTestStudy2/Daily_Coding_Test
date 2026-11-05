/* 

1. 아이디어 : 방문 배열과 이동 방향을 미리 정의 후, i,i부터 아래 -> 오른쪽 -> 위 -> 왼쪽 경로의 원소 위치 수집
            k번 만큼 회전(이동)한 위치에 넣는다 - 모듈러 연산 필요


2. 시간복잡도 : O(2*N*M)

3. 자료구조/알고리즘 : 방향 전환, 배열

 */

class Solution {
    private boolean[][] visited;
    private int[][] ans;
    private int[] dy = {0,1,0,-1};
    private int[] dx = {-1,0,1,0};
    public int[][] rotateGrid(int[][] grid, int k) {
        // m, n은 짝수
        // k 횟수 만큼 왼쪽 회전
        
        visited = new boolean[grid.length][grid[0].length];
        ans = new int[grid.length][grid[0].length];
        int limit = Math.min(grid.length, grid[0].length)/2;
        for(int i=0; i<limit; i++) {
            rotate(i,i,grid,k);
        }

        return ans;
    }

    private void rotate(int y, int x, int[][] grid, int k) {
        List<int[]> list = new ArrayList<>();
        visited[y][x] = true;
        list.add(new int[]{y,x});

        int startY = y;
        int startX = x;

        // 아래 방향
        int dir = 1;
        while(true) {
            int ny = y+dy[dir];
            int nx = x+dx[dir];

            if(ny == startY && nx == startX) break;

            if(ny<0 || nx<0 || ny>=grid.length || nx>=grid[0].length || visited[ny][nx]) {
                dir=(dir+1)%4;
                continue;
            }
            
            y = ny;
            x = nx;

            visited[y][x] = true;
            list.add(new int[]{y,x});
        }

        int size = list.size();
        int move = k%size;

        for(int i=0; i<size; i++) {
            int[] original = list.get(i);
            int[] tmp = list.get((i+move)%size);

            ans[tmp[0]][tmp[1]] = grid[original[0]][original[1]];
        }
    }
}
/*

1. 아이디어 : 바이러스 확산 영역을 파악 후, 가장 많이 확산되는 영역을 벽으로 격리, 
              나머지 영역은 확산하며, 더이상 바이러스가 퍼지지 않을때까지 반복

              1. Area 구조체를 만들어 확산될 영역의 위치와 세울 벽의 개수, 영역의 최초 시작점을 파악
              2. 파악한 정보를 확산될 영역 기준 오름차순으로 정렬하여 첫번째 인덱스는 벽으로 격리, 나머지는 확산을 진행
              3. 더이상 확산될 영역이 없을때까지 반복

2. 시간복잡도 : O((N*M)^2)

3. 자료구조/알고리즘 : bfs + 구현

 */

class Solution {

    private static class Area {
        List<int[]> list;
        int wallCnt;
        int[] pos;

        Area(List<int[]> list, int wallCnt, int[] pos) {
            this.list = list;
            this.wallCnt = wallCnt;
            this.pos = pos;
        }
    }

    private int[][] map;
    private boolean[][] visited;
    private List<Area> countnextInfect;
    private int[] dy = {0,1,0,-1};
    private int[] dx = {1,0,-1,0};
    private int m,n,ans;

    public int containVirus(int[][] isInfected) {
        
        map = isInfected;
        m = map.length;
        n = map[0].length;
        
        while(true) {
            visited = new boolean[m][n];
            countnextInfect = new ArrayList<>();
            for(int i=0; i<m; i++) {
                for(int j=0; j<n; j++) {
                    if(map[i][j] == 0) continue;
                    if(map[i][j] == 1 && !visited[i][j]) countDangerArea(i,j);
                }
            }

            if(countnextInfect.size() == 0) break;

            Collections.sort(countnextInfect, (a,b) -> b.list.size()-a.list.size());
            
            // 확산
            for(int i=0; i<countnextInfect.size(); i++) {
                Area area = countnextInfect.get(i);
                if(i == 0) {
                    ans+=area.wallCnt;
                    Deque<int[]> dq = new ArrayDeque<>();
                    boolean[][] tmpVisited = new boolean[m][n];
                    dq.add(new int[]{area.pos[0], area.pos[1]});
                    tmpVisited[area.pos[0]][area.pos[1]] = true;

                    while(!dq.isEmpty()) {
                        int[] curr = dq.poll();
                        int y = curr[0];
                        int x = curr[1];

                        // 격리체크
                        map[y][x] = 2;

                        for(int dir = 0; dir<4; dir++) {
                            int ny = y + dy[dir];
                            int nx = x + dx[dir];

                            if(ny >= m || nx >= n || ny < 0 || nx < 0) continue;
                            if(tmpVisited[ny][nx] || map[ny][nx] == 0 || map[ny][nx] == 2) continue;

                            tmpVisited[ny][nx] = true;
                            dq.add(new int[]{ny, nx});
                        }
                    }
                }
                else {
                    for(int[] pos : area.list) {
                        int y = pos[0];
                        int x = pos[1];

                        map[y][x] = 1;
                    }
                }
            }
        }
        return ans;
    }

    private void countDangerArea(int startY, int startX) {
        Deque<int[]> dq = new ArrayDeque<>();
        Set<Integer> infectPosition = new HashSet<>();
        int wallCnt = 0;
        List<int[]> list = new ArrayList<>();
        
        dq.add(new int[]{startY,startX});
        visited[startY][startX] = true;

        while(!dq.isEmpty()) {
            int[] curr = dq.poll();
            int y = curr[0];
            int x = curr[1];

            for(int dir=0; dir<4; dir++) {
                int ny = y + dy[dir];
                int nx = x + dx[dir];

                if(ny >= m || nx >= n || ny < 0 || nx < 0) continue;
                if(visited[ny][nx] || map[ny][nx] == 2) continue;
                if(map[ny][nx] == 0) {
                    if(!infectPosition.contains(ny*n+nx)) {
                        infectPosition.add(ny*n+nx);
                        list.add(new int[]{ny,nx});
                    } 
                    wallCnt++;
                    continue;
                }
                
                dq.add(new int[]{ny,nx});
                visited[ny][nx] = true;
            }
        }
        
        countnextInfect.add(new Area(list, wallCnt, new int[]{startY, startX}));
    }
}
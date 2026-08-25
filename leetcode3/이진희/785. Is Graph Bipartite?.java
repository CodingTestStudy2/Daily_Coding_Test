/*

1. 아이디어 : 인접한 노드는 같은 그룹이 되면 안된다. bfs 로 모든 시작점을 탐색해서, 인접한 노드끼리 같은 그룹일 경우 false

2. 시간복잡도 : O(N+E)

3. 자료구조/알고리즘 : BFS

 */

class Solution {
    private List<List<Integer>> g = new ArrayList<>();
    private int n;
    private int[] visited;
    public boolean isBipartite(int[][] graph) {
        
        n = graph.length;
        visited = new int[n+1];

        for(int i=0; i<n; i++) g.add(new ArrayList<>());
        
        for(int i=0; i<graph.length; i++) {
            for(int j=0; j<graph[i].length; j++) {
                g.get(i).add(graph[i][j]);
            }
        }

        // 이웃한 노드끼리 다른 그룹

        for(int i=0; i<n; i++) {
            if(visited[i] != 0) continue;
            if(!bfs(i)) return false; 
        }

        return true;
    }

    private boolean bfs(int start) {
        Deque<Integer> dq = new ArrayDeque<>();

        dq.add(start);
        visited[start] = 1;

        while(!dq.isEmpty()) {
            int num = dq.poll();
            for(int node : g.get(num)) {
                if(visited[node] == 0) {
                    visited[node] = -visited[num];
                    dq.add(node);
                }
                else if (visited[num] == visited[node]) return false; 
            }
        }  

        return true;      
    }
}
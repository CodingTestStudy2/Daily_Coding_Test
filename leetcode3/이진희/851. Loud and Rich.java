/*

1. 아이디어 : 각 노드기준 더 돈이 많거나 같은 노드의 집합에서 가장 quiet값이 작은 인덱스 선택 
             dag구조 활용, 방향이 있고 cycle이 없는 그래프이므로, 위상정렬 사용 가능
             각 노드별로 더 작은 값들을 연결, 이때 각 노드의 degree(더 큰 값의 개수)를 같이 구해 degree가 0인 노드 파악 
             큰 -> 작 순으로 그래프를 탐색하므로, 매 이동마다 가장 최선의값을 줄 수 있음
             
             이때 degree[i] == 0인값만 deque에 넣는 이유는, 현 노드 기준 더 큰 모든 노드의 최적값을 계산해야 하기 때문


2. 시간복잡도 : O(V + E)

3. 자료구조/알고리즘 : bfs + 위상정렬

 */


class Solution {
    
    private List<List<Integer>> dag = new ArrayList<>();
    private int[] ans;
    private int[] degree;

    public int[] loudAndRich(int[][] richer, int[] quiet) {
        // richer[0]>richer[1]
        // ans[x] = y 
        // y는 x보다 돈이 같거나  많은 그룹(본인 포함), 그중 quite가 가장 작아야함 

        // graph 구조 , 사이클 없음, 단방향 -> DAG

        ans = new int[quiet.length];
        degree = new int[quiet.length];

        for(int i=0; i<quiet.length; i++) {
            dag.add(new ArrayList<>());
        }

        for(int[] r : richer) {
            dag.get(r[0]).add(r[1]);
            degree[r[1]]++;
        }

        bfs(quiet);

        return ans;
    }

    void bfs(int[] quiet) {
        Deque<Integer> dq = new ArrayDeque<>();

        for(int i=0; i<quiet.length; i++) {
            if(degree[i] == 0) dq.add(i);
            ans[i] = i;
        }

       while(!dq.isEmpty()) {

            int cur = dq.poll();

            for(int node : dag.get(cur)) {
                
                if(quiet[ans[cur]]<quiet[ans[node]]) ans[node] = ans[cur];
                degree[node]--;
                
                if(degree[node] == 0) dq.add(node);
            }
       }
    }
}
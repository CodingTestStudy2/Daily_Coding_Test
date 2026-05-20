/*

1. 아이디어 : tree 구조의 특성을 활용
            1차: 처음에는 플로이드 워셜 알고리즘을 떠올렸지만, O(N^3)의 시간복잡도에 풀이가 가능한 최대 노드 개수는 500 이하므로 탈락 (여긴 최대 3만)
            2차: tree 구조로 되어있는것을 확인, 두개의 dfs + dp를 활용하여 풀이
                 dfs1: Bottom-Up: 맨 아래 리프 노드 부터 올라가며 특정 노드의 서브 노드 개수 계산
                 dfs2: Top-Down: 루트부터 리프 노드까지 내려가며, 최종 dp(각 노드 기준 모든 노드 사이의 거리) 계산

2. 시간복잡도 : O(N) + O(N) + O(N) => O(N)

3. 자료구조/알고리즘 : dfs + dp

 */

class Solution {
    private List<List<Integer>> graph;
    private int[] cnt; // 특정 노드에서 서브트리 노드 개수
    private int[] dp;
    private int totalNodes;

    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        // 특정 노드에서 모든 노드 사이의 거리의 합 전부
        // 최대 n은 3만개
        // 무방향 그래프

        graph = new ArrayList<>();
        cnt = new int[n];
        dp = new int[n];
        totalNodes = n;

        for(int i=0; i<n+1; i++) graph.add(new ArrayList<>());

        for(int[] edge: edges) {
            int y = edge[0];
            int x = edge[1];

            graph.get(y).add(x);
            graph.get(x).add(y);
        }
        
        // 서브 노드가 하나도 없어도, 자기 자신이 존재하므로
        Arrays.fill(cnt, 1);
        dfs1(0, -1);
        dfs2(0, -1);

        return dp;
    }

    // Bottom-Up
    // 통상 dfs면 visited를 활용하지만, tree구조 인걸 파악하여 
    // if(child == parent) continue;로 간소화
    private void dfs1(int node, int parent) {
        for(int child: graph.get(node)) {
            if(child == parent) continue;
            dfs1(child, node);

            cnt[node] += cnt[child];
            dp[node] += dp[child] + cnt[child];
        }
    }

    // Top-Down
    // bfs도 가능하나 거의 차이가 없어 dfs로 계산
    private void dfs2(int node, int parent) {
        for(int child: graph.get(node)) {
            if(child == parent) continue;
            
            // 서브 노드로 이동할 때 가까워지는 노드 수만큼 빼고, 멀어지는 노드 수만큼 더함
            dp[child] = dp[node] - cnt[child] + (totalNodes - cnt[child]);
            dfs2(child, node);
        }
    }
}
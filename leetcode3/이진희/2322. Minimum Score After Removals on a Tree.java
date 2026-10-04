/*
1. 아이디어: 트리 구조 원리 사용
            주어진 노드와 간선을 트리 구조로 저장하여 루트를 0으로 잡고 탐색

            이때 각 노드를 루트로하는 XOR연산의 합을 미리 계산

            이후, edges[][]를 완전탐색하여 2개의 제거할 간선을 고르고, 3개의 경우의 수를 기준으로 값을 계산

2. 시간복잡도: O(E) + O(V^2) + O(E^2) => O(V^2) (V ~= E)

3. 자료구조/알고리즘: DFS, Tree

*/

class Solution {
    private List<List<Integer>> tree = new ArrayList<>();
    private int n;
    private int[] xorSum;
    private int[] depths;
    private boolean[][] isAncestor;

    public int minimumScore(int[] nums, int[][] edges) {
        // 모든 연결된 간선중 2개 제거
        // 가능한 모든 경우의 수 중 최소 점수

        int ans = Integer.MAX_VALUE;
        n = nums.length;
        // 각 노드 기준 모든 서브트리의 xor값
        xorSum = new int[n];
        // 루트 기준 떨어진 길이
        depths = new int[n];
        // 조상 여부
        isAncestor = new boolean[n][n];

        for(int i=0; i<n; i++) {
            tree.add(new ArrayList<>());
        }
        for(int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];

            tree.get(a).add(b);
            tree.get(b).add(a);
        } 

        // 각 노드기준 모든 xor연산 합 계산
        dfs(0, -1, nums, 0);    

        for(int i=0; i<edges.length-1; i++) {
            for(int j=i+1; j<edges.length; j++) {
                int[] edge1 = edges[i];
                int[] edge2 = edges[j];

                int child1 = depths[edge1[0]] > depths[edge1[1]] ? edge1[0] : edge1[1];
                int child2 = depths[edge2[0]] > depths[edge2[1]] ? edge2[0] : edge2[1];

                int a= xorSum[child1];
                int b= xorSum[child2];
                int c= xorSum[0];                

                if(isAncestor[child1][child2]) {
                    //xorSum[child2]
                    //xorSum[child1]^xorSum[child2]
                    //xorSum[0]^xorSum[child1]

                    a ^= xorSum[child2];
                    c ^= xorSum[child1];
                }
                else if(isAncestor[child2][child1]) {
                    //xorSum[child1]
                    //xorSum[child2]^xorSum[child1]
                    //xorSum[0]^xorSum[child2]

                    b ^= xorSum[child1];
                    c ^= xorSum[child2];
                }
                else {
                    //xorSum[child1]
                    //xorSum[child2]
                    //xorSum[0]^xorSum[child1]^xorSum[child2]

                    c = c^a^b;
                }

                ans = Math.min(ans, Math.max(a,Math.max(b,c)) - Math.min(a,Math.min(b,c)));
                if(ans == 0) return 0;
            }
        }   

        return ans;
    }

    private int dfs(int curr, int parent, int[]nums, int depth) {
        int currXor = nums[curr];
        depths[curr] = depth;

        for(int next : tree.get(curr)) {
            if(next == parent) continue;

             for(int i = 0; i < n; i++) {
                if(isAncestor[i][curr]) isAncestor[i][next] = true;
            }
            isAncestor[curr][next] = true;
            currXor ^= dfs(next, curr, nums, depth+1);
        }

        xorSum[curr] = currXor;
        return currXor; 
    }
}
/*

1. 아이디어 : 
- 그래프에서 k개의 컴포넌트를 남기기 위한 최소 비용 구하기
- 간선 비용 오름차순 정렬 후, 비용이 작은 간선부터 순서대로 연결
- Union-Find를 통해 두 노드를 연결할 때마다 연결(간선) 수를 증가시키며, n-k개 연결 시점의 가중치 반환

2. 시간복잡도 : O(E log E)

3. 자료구조/알고리즘 : 크루스칼 알고리즘 (Union-Find)

 */

class Solution {
    private int[] parent;
    public int minCost(int n, int[][] edges, int k) {

        if(edges.length == 0) return 0;

        // 가중치 기준 오름차순 정렬
        Arrays.sort(edges, (a,b) -> Integer.compare(a[2],b[2]));

        parent = new int[n];
        Arrays.fill(parent, -1);

        int link = 0;

        for(int i=0; i<edges.length; i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            int w = edges[i][2];

            if(union(a,b)) link++;

            if(link == n-k) return w; 
        }

        return 0;
    }

    private int find(int x) {
        if(parent[x] < 0) return x;
        return parent[x] = find(parent[x]);
    }

    private boolean union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if(rootX == rootY) return false;

        if(parent[rootX] > parent[rootY]) parent[rootX] = rootY;
        else if(parent[rootX] < parent[rootY]) parent[rootY] = rootX;
        else {
            parent[rootX] = rootY;
            parent[rootY]--;
        }

        return true;
    }
}
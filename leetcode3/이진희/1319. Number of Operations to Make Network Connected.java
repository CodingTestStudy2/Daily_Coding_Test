/*

1. 아이디어 : 신장트리 구하기. 각 연결시 가중치가 없으므로 union-find로 신장트리를 구할 수 있는지 체크한다.
            1. untion(a,b)로 연결됐는지 확인후 연결됐다면 카운트
            2. 모든 connections 배열을 체크했을 때 cnt==(n-1) 이면 전부 연결됐으므로 0 리턴
            3. cnt가 (n-1)보다 작다면 n-1-cnt만큼의 선을 옮겨야함. 그러니 답은 (n-1-cnt)
            4. connections 배열 크기가 n-1보다 작다면 아예 신장트리를 만들 수 없으므로 미리 체크한다

2. 시간복잡도 : O(N + MA(N)) (A(N)은 거의 상수)

3. 자료구조/알고리즘 : 신장트리 + union-find

 */
class Solution {
    int[] parent;
    public int makeConnected(int n, int[][] connections) {

        if(connections.length < (n-1)) return -1; 

        parent = new int[n];
        Arrays.fill(parent, -1);
        int cnt = 0;

        for(int i=0; i<connections.length; i++) {
            int a = connections[i][0];
            int b = connections[i][1];

            if(union(a,b)) cnt++;
            if(cnt == (n-1)) return 0; 
        }

        return (n-1)-cnt;
    }

    private boolean union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if(rootA == rootB) return false;

        if(parent[rootA]>parent[rootB]) parent[rootA] = rootB;
        else if(parent[rootA]<parent[rootB]) parent[rootB] = rootA;
        else {
            parent[rootA] = rootB;
            parent[rootB]--;
        }

        return true;
    }

    private int find(int x) {
        if(parent[x] < 0) return x;
        return parent[x] = find(parent[x]);
    }
}
/*
1. 아이디어: 문자열 idx 기준 swap가능한 idx그룹을 모아 사전순으로 정렬 후 idx그룹 의 idx에 배치
           Group안의 모든 원소를 사전순 정렬만 하면 되므로 BFS 구조 대신 union-find 구조가 적절한것 같음
           매번 원소를 list에 저장해서 sort하므로 최적화 필요

2. 시간복잡도: O(nlogn+m)

3. 자료구조/알고리즘: BFS, 정렬

*/

class Solution {
    private List<List<Integer>> graph = new ArrayList<>();
    private boolean[] visited;
    private int len;

    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        // 사전식으로 가장 작은 문자열 만들기

        len = s.length();

       for(int i=0; i<len; i++) graph.add(new ArrayList<>());
       visited = new boolean[len];

       for(List<Integer> pair : pairs) {
            int y = pair.get(0);
            int x = pair.get(1);

            graph.get(y).add(x);
            graph.get(x).add(y);
       }

       char[] ans = new char[len];

       for(int i=0; i<len; i++) {
            if(visited[i]) continue;
            
            List<Integer> group = bfs(i);
            List<Character> alphabet = new ArrayList<>();

            for(int g : group) {
                alphabet.add(s.charAt(g));
            }

            Collections.sort(group);
            Collections.sort(alphabet);

            for(int g=0; g<group.size(); g++) {
                ans[group.get(g)] = alphabet.get(g);
            }
       }

       return String.valueOf(ans);
    }

    private List<Integer> bfs(int start) {
        Deque<Integer> dq = new ArrayDeque<>();
        dq.add(start);
        visited[start] = true;

        List<Integer> group = new ArrayList<>();
        group.add(start);

        while(!dq.isEmpty()) {
            int node = dq.poll();

            for(int next : graph.get(node)) {
                if(visited[next]) continue;
                dq.add(next);
                group.add(next);
                visited[next] = true;
            }
        }

        return group;
    }
}
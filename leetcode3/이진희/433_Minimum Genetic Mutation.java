/*

1. 아이디어 : 그래프 탐색 활용
              유전자 변형은 한번에 한글자, startGene -> endGene로 변경 가능해야 한다
              graph형태로 각 문자열에서 변경 가능한 문자열을 미리 저장하고, 탐색한다

2. 시간복잡도 : O(B) + O(B)^2 + O(B) = O(B^2) 
                B = bank.length()+1

3. 자료구조/알고리즘 : BFS, Set, Map

 */

class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        Map<String, List<String>> graph = new HashMap<>();
        List<String> list = new ArrayList<>();
        
        Set<String> visited = new HashSet<>(); 
        
        list.add(startGene);
        for(String s : bank) {
            list.add(s);
        }

        for(String s : list) {
            graph.put(s, new ArrayList<>());
        }

        for(int i = 0; i < list.size(); i++) {
            for(int j = i + 1; j < list.size(); j++){
                String first = list.get(i);
                String second = list.get(j);
                if(diffOne(first, second)) {
                    graph.get(first).add(second);
                    graph.get(second).add(first);
                }
            }
        }

        return bfs(graph, visited, startGene, endGene);
    }

    private boolean diffOne(String first, String second) {
        int diff = 0;

        for(int i = 0; i < first.length(); i++) {
            if(first.charAt(i) != second.charAt(i)) diff++;
        }

        return diff == 1;
    }

    private int bfs(Map<String, List<String>> graph, Set<String> visited, String startGene, String endGene) {
        Deque<String> dq = new ArrayDeque<>();
        
        dq.add(startGene);
        visited.add(startGene);
        int mutations = 0;
        
        while(!dq.isEmpty()) {
            int size = dq.size();
            
            for(int i = 0; i < size; i++) {
                String curr = dq.poll();
                
                if(curr.equals(endGene)) return mutations;
                
                for(String next : graph.get(curr)) {
                    if(!visited.contains(next)) {
                        visited.add(next);
                        dq.add(next);
                    }
                }
            }
            mutations++;
        }
        
        return -1;
    }
}
// 인접한 노드는 다른 색

class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] color = new int[graph.length];

        for (int i = 0; i<graph.length; i++) {
            if (color[i] != 0) continue;

            Queue<Integer> queue = new LinkedList<>();
            queue.offer(i);
            color[i] = 1;

            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int next : graph[node]) {
                    if (color[next] == color[node]) return false;
                    else if (color[next] == 0) {
                        color[next] = -color[node];
                        queue.offer(next);
                    }
                }
            }
        }
        return true;
    }
}

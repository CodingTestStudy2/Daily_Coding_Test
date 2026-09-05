class Solution {
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        int n = quiet.length;
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        // richer[i] = [a, b] : a는 b보다 부자 -> b는 a에게 정보를 받을 수 있음
        for (int[] r : richer) {
            graph.get(r[1]).add(r[0]);
        }

        int[] answer = new int[n];
        Arrays.fill(answer, -1);

        for (int i = 0; i < n; i++) {
            dfs(i, graph, quiet, answer);
        }

        return answer;
    }

    private int dfs(int person, List<List<Integer>> graph, int[] quiet, int[] answer) {
        if (answer[person] != -1) {
            return answer[person];
        }

        answer[person] = person; // 자기 자신이 일단 후보

        for (int richerPerson : graph.get(person)) {
            int candidate = dfs(richerPerson, graph, quiet, answer);
            if (quiet[candidate] < quiet[answer[person]]) {
                answer[person] = candidate;
            }
        }

        return answer[person];
    }
}

/*
 *   dp[i][j][k] = boxes[i..j]를 지울 때, boxes[i] 바로 앞에 boxes[i]와
 *                 같은 색 박스가 k개 딸려 있다고 가정했을 때의 최대 점수
 *
 *   두 가지 선택 중 큰 값을 취한다:
 *     (1) 앞에 붙은 k개 + boxes[i]를 지금 바로 제거
 *         →  (k+1)*(k+1) + dp[i+1][j][0]
 *     (2) i+1..j 중 boxes[i]와 같은 색인 m을 찾아, 사이 구간을 먼저 비우고
 *         boxes[i]를 boxes[m]에 이어 붙여 나중에 함께 제거
 *         →  dp[i+1][m-1][0] + dp[m][j][k+1]
 *
 *   최적화: boxes[i]와 색이 같은 연속 구간을 미리 k에 흡수시켜 중복 계산을 줄인다.
 *
 *   * dp 값 0은 "미계산" 표시로 안전하다. i<=j이면 박스가 최소 1개 있어
 *     제거 시 최소 1점을 얻으므로, 유효한 답이 0이 되는 경우는 없다.
 */
class Solution {
    public int removeBoxes(int[] boxes) {
        int n = boxes.length;
        int[][][] dp = new int[n][n][n];
        return dfs(boxes, dp, 0, n - 1, 0);
    }

    private int dfs(int[] boxes, int[][][] dp, int i, int j, int k) {
        if (i > j) return 0;
        if (dp[i][j][k] != 0) return dp[i][j][k];

        // 최적화: boxes[i]와 같은 색이 연속되면 미리 k에 흡수
        int i0 = i, k0 = k;
        while (i < j && boxes[i] == boxes[i + 1]) {
            i++;
            k++;
        }

        // 선택 (1): 앞에 붙은 k개 + boxes[i]를 지금 제거
        int res = (k + 1) * (k + 1) + dfs(boxes, dp, i + 1, j, 0);

        // 선택 (2): 같은 색 m을 찾아 이어 붙이기
        for (int m = i + 1; m <= j; m++) {
            if (boxes[m] == boxes[i]) {
                res = Math.max(res,
                        dfs(boxes, dp, i + 1, m - 1, 0) + dfs(boxes, dp, m, j, k + 1));
            }
        }

        dp[i0][j][k0] = res;  // 흡수 전 원래 인덱스(i0, k0)로 캐싱
        return res;
    }
}

/*
1. 아이디어:
   - 첫번째 두번째 손가락 위치와 현재 문자열중 idx 위치를 dp 상태로 체크
   - 모든 경우의 수를 전부 구해야하므로 dp로 최적화 필요

2. 시간복잡도: O(n×26^2)

3. 자료구조/알고리즘: DP
*/

class Solution {
    private static final int[][] pos = {
        {0,0},{0,1},{0,2},{0,3},{0,4},{0,5},
        {1,0},{1,1},{1,2},{1,3},{1,4},{1,5},
        {2,0},{2,1},{2,2},{2,3},{2,4},{2,5},
        {3,0},{3,1},{3,2},{3,3},{3,4},{3,5},
        {4,0},{4,1}
    };

    private String wordStr;
    private Integer[][][] memo;

    public int minimumDistance(String word) {
        wordStr = word;

        memo = new Integer[27][27][word.length()];

        return top_down(-1, -1, 0);
    }

    private int top_down(int left, int right, int idx) {
        if (idx == wordStr.length()) return 0;

        if (memo[left+1][right+1][idx] != null) {
            return memo[left+1][right+1][idx];
        }

        int target = wordStr.charAt(idx)-'A';

        int leftCost = 0;
        if (left != -1) leftCost = calDist(left, target);
        int useLeft = leftCost + top_down(target, right, idx+1);

        int rightCost = 0;
        if (right != -1) rightCost =calDist(right, target);
        int useRight = rightCost + top_down(left, target, idx+1);

        memo[left+1][right+1][idx] = Math.min(useLeft, useRight);

        return memo[left+1][right+1][idx];
    }

    private int calDist(int a, int b) {
        return Math.abs(pos[a][0]-pos[b][0]) + Math.abs(pos[a][1]-pos[b][1]);
    }
}
/*

1. 아이디어 : 각 정점의 개수 구하기

2. 시간복잡도 : O(N^2)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int[] findDegrees(int[][] matrix) {
        int n = matrix[0].length;

        int ans[] = new int[n];
        for(int k=0; k<n; k++) {
            for(int i=0; i<n; i++) {
                if(matrix[k][i] == 0) continue;
                ans[k]++;
            }
        }
        return ans;
    }
}
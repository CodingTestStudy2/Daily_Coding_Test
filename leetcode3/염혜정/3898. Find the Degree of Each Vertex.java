// 완전탐색
// o(n^2)

class Solution {
    public int[] findDegrees(int[][] matrix) {
        int[] result = new int[matrix.length];
        for (int i = 0; i<matrix.length; i++) {
            for (int k = 0; k<matrix[0].length; k++) {
                if (matrix[i][k] == 1) result[i]++;
            }
        }
        return result;
    }
}

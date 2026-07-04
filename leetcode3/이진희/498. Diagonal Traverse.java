/* 

1. 아이디어 : 같은 대각선은 r+c가 같다는 특징이 있으므로 대각선 번호 k를 0부터 m + n - 2까지 순회한다
              if문을 사용하여 어떤 방향으로 순회할지 결정한다
              k가 짝수이면 아래에서 위로, k가 홀수이면 위에서 아래로 이동한다

2. 시간복잡도 : O(M*N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;

        int[] ans = new int[m*n];
        int idx = 0;

        for (int k=0; k < m+n-1; k++) {
            if (k%2 == 0) {
                for (int r=m-1; r>=0; r--) {
                    int c = k-r;
                    if (c>=0 && c<n) {
                        ans[idx++] = mat[r][c];
                    }
                }
            } else {
                for (int r=0; r<m; r++) {
                    int c = k-r;
                    if (c>=0 && c<n) {
                        ans[idx++] = mat[r][c];
                    }
                }
            }
        }
        return ans;
    }
}
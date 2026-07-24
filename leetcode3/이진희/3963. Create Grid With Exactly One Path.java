/*

1. 아이디어 : 우, 하단으로만 이동 가능할때 0,0 -> m-1, n-1로 가는 단 하나의 루트를 만들어라
              ㄴ자로 이동하는 루트를 고정으로 생성

2. 시간복잡도 : O(n+m)

3. 자료구조/알고리즘 : 규칙

 */

class Solution {
    public String[] createGrid(int m, int n) {
        // 단 하나의 root 만들기
        int[][] map = new int[m][n];
        for(int i=0; i<m; i++) {
            Arrays.fill(map[i], 1);
        }

        for(int i=0; i<m; i++) map[i][0] = 0;
        for(int i=0; i<n; i++) map[m-1][i] = 0;

        String[] ans = new String[m];

        for(int i=0; i<m; i++) {
            StringBuilder sb = new StringBuilder();
            for(int j=0; j<n; j++) {
                if(map[i][j] == 0) sb.append('.');
                else sb.append('#');
            }
            ans[i] = sb.toString();
        }

        return ans;
    }
}
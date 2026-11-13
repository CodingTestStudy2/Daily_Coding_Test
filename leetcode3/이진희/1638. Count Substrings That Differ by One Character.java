/*
1. 아이디어: 각 문자열에서 s는 i까지, t는 j까지의 부분 문자열에서 같은 상태과 다른 상태를 따로 분리해 관리
            - 현재 위치 문자가 다를때 이전까지 문자열이 몇글자가 연속으로 같았는지 알기위해 dp를 2개로 정의

2. 시간복잡도: O(n*m)

3. 자료구조/알고리즘: DP

*/

class Solution {
    public int countSubstrings(String s, String t) {
        int n = s.length();
        int m = t.length();

        int[][] same = new int[n+1][m+1];
        int[][] diff = new int[n+1][m+1];

        int ans = 0;

        for(int i=1; i<=n; i++) {
            for(int j=1; j<=m; j++) {
                char sc = s.charAt(i-1);
                char tc = t.charAt(j-1);

                if(sc == tc) {
                    same[i][j] = same[i-1][j-1] +1;
                    diff[i][j] = diff[i-1][j-1];
                }
                else {
                    same[i][j] = 0;
                    diff[i][j] = same[i-1][j-1] + 1;
                }

                ans += diff[i][j];
            }
        }

        return ans;
    }
}
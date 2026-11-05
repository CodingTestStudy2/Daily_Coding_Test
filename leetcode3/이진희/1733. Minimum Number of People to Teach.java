/* 

1. 아이디어 : 각 사람별로 가능한 언어를 별로의 boolean 배열에 저장, 이후 친구 관계 배열을 순환하며 서로 소통이 되지 않는 언어만 need 배열에 별도 기록
             다음 완전탐색으로 n=1 ~ n까지 전부 돌며 각 언어에서 가르쳐야 하는 인원을 체크 후 최소 인원으로 return

2. 시간복잡도 : O(N*M)

3. 자료구조/알고리즘 : 그리디, 배열 사용

 */

class Solution {
    // 언어중 하나를 선택해서 가르쳐야 하는 최소 인원
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
       int m = languages.length; 

       boolean[][] knownLanguages = new boolean[m+1][n+1];

       for(int i=0; i<languages.length; i++) {
            for(int lang : languages[i]) {
                knownLanguages[i+1][lang] = true;
            }
       }

       boolean[] need = new boolean[m+1];

       for(int i=0; i<friendships.length; i++) {
            int a = friendships[i][0];
            int b = friendships[i][1];

            boolean canTalk = false;
            
            for(int j=1; j<=n; j++) {
                if(knownLanguages[a][j] && knownLanguages[b][j]) {
                    canTalk = true;
                    break;
                }
            }

            if(!canTalk) {
                need[a] = true;
                need[b] = true;
            }
       }

       int ans = 1000;

       for(int i=0; i<=n; i++) {
            int tmp = 0;

            for(int j=0; j<=m; j++) {
                if(need[j] && !knownLanguages[j][i]) tmp++;
            }

            ans = Math.min(ans, tmp);
       }

        return ans;
    }
}
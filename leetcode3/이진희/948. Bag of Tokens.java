/* 

1. 아이디어 : face-up과 face-down의 규칙을 파악후, 그리디로 계산
              - face-up: powers 이하의 가장 낮은 점수 
              - face-down: 가장 높은 점수 
2. 시간복잡도 : O(NlogN) + O(N)

3. 자료구조/알고리즘 : 투포인터 , 정렬 (그리디)

 */

class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        // face-up: power가 tokens[i] 이상이면 -> tokens[i]만큼 power를 잃고, 1점+
        // face-down: score가 1 이상이면, tokens[i] 만큼 powers를 얻고, 1점 감점
        // 가능한 가장 높은 score

        // face-up: powers 이상의 가장 낮은 점수 
        // face-down: tokens중 가장 높은 점수 

        Arrays.sort(tokens);

        int l=0;
        int r=tokens.length-1;
        int score = 0;
        int maxScore = 0;

        while(l<=r) {
            // face-up
            if(tokens[l]<=power) {
                power-=tokens[l];
                score++;
                l++;
                maxScore = Math.max(score, maxScore);
            }
            // face-down
            else if(score>0) {
                power+=tokens[r];
                score--;
                r--;
            }
            else break;
        }

         return maxScore;
    }
}
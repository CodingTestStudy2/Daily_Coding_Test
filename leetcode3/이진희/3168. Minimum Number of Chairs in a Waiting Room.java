/*

1. 아이디어 : 최소 의자의 개수 찾기
              현재 인원과, 현재 놓아진 의자 수를 분리하여 확인

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 조건문

 */

class Solution {
    public int minimumChairs(String s) {
        // 최소 의자의 개수
        // E, L

        int currChairCnt = 0;
        int currPeopleCnt = 0;
        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            if(c == 'E') {
                currPeopleCnt++;
                if(currChairCnt >= currPeopleCnt) continue;
                else currChairCnt++;
            }
            else currPeopleCnt--;
        }

        return currChairCnt;
    }
}
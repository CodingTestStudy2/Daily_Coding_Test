/*
1. 아이디어:
   - 연속적으로 8시간 이상 일한날이 많은구간의 최대 길이 구하기
   - 완전탐색을 통해, 8시간 기준날을 체크해서 8시간 일한 날이 더 많으면 갱신
   - 더 적으면 뒤로 돌아가면서 연속구간 재갱신

2. 시간복잡도: O(N^2)

3. 자료구조/알고리즘: 완전탐색, 누적합
*/

class Solution {
    public int longestWPI(int[] hours) {
        // 9시간 이상 일하면 지침

        // 근데 피곤한 날이 피곤하지 않은 날보다 많아야 well-performing

        // 최대 구간 길이 구하기

        int over = 0;
        int good = 0;
        int ans = 0;

        for(int i=0; i<hours.length; i++) {
            int hour = hours[i];

            if(hour>8) over++;
            else good++;

            // 일한날이 더 많음
            if(over > good) ans = i+1;
            else {
                int tmpOver = over;
                int tmpGood = good;

                for(int j=0; j<=i; j++) {
                    if(hours[j] > 8) tmpOver--;
                    else tmpGood--;

                    if(tmpGood < tmpOver) {
                        ans = Math.max(ans, i-j);
                        break;
                    }
                }
            }
        }

        return ans;
    }
}
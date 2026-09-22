/* 

1. 아이디어 : 거스름돈을 줄 수 있는지 체크 
            10$ -> 5$ 1장
            20$ -> 5$ 3장 or 10$ + 5$ 

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색, 조건문 

 */

class Solution {
    public boolean lemonadeChange(int[] bills) {

        // 5 10
        int[] money = new int[2];

        for(int i=0; i<bills.length; i++) {
           int pay = bills[i];

           if(pay == 5) money[0]++;
           else if(pay == 10) {
                if(money[0] == 0) return false;
                money[1]++;
                money[0]--;
           }
           else {
                // 5$ 3장 or 10$ + 5$
                if(money[0]>0 && money[1]>0) {
                    money[0]--;
                    money[1]--;
                }
                else if (money[0] > 2) money[0] -=3;
                else return false;
           }
        }

        return true;
    }
}
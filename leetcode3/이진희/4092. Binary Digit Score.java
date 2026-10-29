/*

1. 아이디어 : 2진법으로 변환 후 1의 개수 세기

2. 시간복잡도 : O(logN)

3. 자료구조/알고리즘 : 진법변환

 */

class Solution {
    public int calculateScore(int a, int b) {
        int s1 = countBit(a);
        int s2 = countBit(b);

        if(s1>=s2) return s1*s2;
        return s2/s1;
    }

    private int countBit(int num) {
        int cnt = 0;
        while(num>0) {
            if(num%2==1) cnt++;
            num/=2; 
        }

        return cnt;
    }
}
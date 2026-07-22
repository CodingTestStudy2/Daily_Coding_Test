/*

1. 아이디어 : n의 각 자릿수 개수를 파악후 값을 구한다.

2. 시간복잡도 : O(9) + O(10) => O(1)

3. 자료구조/알고리즘 : 카운팅 배열

 */

class Solution {
    public int digitFrequencyScore(int n) {
        int[] num = new int[10];
        while(n>0) {
            int tmp = n%10;
            num[tmp]++;
            n/=10;
        }

        int ans = 0;
        for(int i=0; i<10; i++) {
            if(num[i]==0) continue;
            ans+=num[i]*i;
        }

        return ans;
    }
}
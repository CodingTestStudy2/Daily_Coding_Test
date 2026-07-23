/*

1. 아이디어 : 수식을 만족하는 x의 값 구하기

2. 시간복잡도 : O(200) // n=100 k=100

3. 자료구조/알고리즘 : 수학

 */

class Solution {
    public int sumOfGoodIntegers(int n, int k) {
        // x는 양수 
        // k+n >= x >= n-k
        int ans = 0;
        int start = n-k>0 ? n-k : 1;
        int end = n+k;
        
        for(int i = start; i<= end; i++) {
            if((n&i) == 0) ans+=i;
        }

        return ans;
    }
}
// 2진수를 구하고 오직 한 쌍의 11만 존재하여야 함
// O(logn)

class Solution {
    public boolean consecutiveSetBits(int n) {
        int cnt = 0;
        int pre = 0;
        while (n>0) {
            if (pre == 1 && n%2 ==1) cnt++;
            pre = n%2;
            n /= 2;
        }
        
        return cnt == 1;
    }
}

/*

1. 아이디어 : 콤마가 생기는 기준점(1,000, 1,000,000 등)을 초과하는 숫자의 개수를 누적해서 더함

2. 시간복잡도 : O(logN)

3. 자료구조/알고리즘 : 단순계산

 */

class Solution {
    public int countCommas(int n) {
        long totalCommas = 0;
        
        for (long i = 1000; i <= n; i *= 1000) {
            totalCommas += (n - i + 1);
        }
        
        return (int)totalCommas;
    }
}
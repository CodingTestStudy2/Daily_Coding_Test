// 0을 제외하고 1, 11, 111, 1111... (2^1 - 1, 2^2 - 1, 2^3 -1)
// o(log n)

class Solution {
    public int countMonobit(int n) {
        int cnt = 1; // 0은 무조건 포함
        int num = 1;
        while (num <= n) {
            cnt++;
            num = num * 2 + 1;
        }
        return cnt;
    }
}

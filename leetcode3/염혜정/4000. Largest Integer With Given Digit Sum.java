// 9로 나눠가며 9부터 채우고 나머지 값 붙이기
// 무조건 n차수 맞추기
// O(n)

class Solution {
    public int largestInteger(int n, int s) {
        if (s==0) return 0;
        if (s > n*9) return -1;

        StringBuilder sb = new StringBuilder();
        int cnt_9 = s / 9;
        int r = s % 9;
        for (int i = 0; i<cnt_9; i++) {
            sb.append("9");
        }

        int digitCnt = cnt_9;
        if (r != 0) {
            sb.append(r);
            digitCnt++;
        }

        for (int i = digitCnt; i<n; i++) {
            sb.append("0");
        }

        int result = Integer.parseInt(sb.toString());
        return result;
    }
}

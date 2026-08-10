// 10진수 -> 2진수
// 1과 0을 서로 바꿈
// 2진수 -> 10진수


class Solution {
    public int findComplement(int num) {
        StringBuilder sb = new StringBuilder();
        while (num>0) {
            int bit = num%2;
            // 0과 1을 체인지
            if (bit == 0) sb.append(1);
            else sb.append(0);
            num /= 2;
        }

        String ten = sb.toString();
        int result = ten.charAt(0) - '0';
        if (ten.length() == 1) return result;

        for (int i = 1; i<ten.length(); i++) {
            int digit = ten.charAt(i) - '0';
            if (digit == 0) continue;
            int pow = 1;
            for (int cnt = 0; cnt<i; cnt++) {
                pow *= 2;
            }
            result += pow;
        }

        return result;
    }
}

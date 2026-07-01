// 전체합을 먼저 구한 다음에 한쪽 합만 구하고 빼주면 나머지 합도 구할 수 있음
// 시간복잡도 O(n)

class Solution {
    public boolean scoreBalance(String s) {
        // a ~ b 97 ~ 122
        int total = 0;
        for (char c : s.toCharArray()) total += c - 96;
        
        int left_sum = 0;
        for (int i = 0; i<s.length()-1; i++) {
            left_sum += s.charAt(i)-96;
            int right_sum = total - left_sum;

            if (left_sum == right_sum) {
                return true;
            }
        }
        return false;
    }
}

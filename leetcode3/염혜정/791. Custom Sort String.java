// 1. 알파벳 별로 등장 횟수를 카운트
// 2. order 순서에 맞게 카운트한 알파벳 나열
// 3. order에 포함되지 않은 알파벳 추가

// O(n+m)

class Solution {
    public String customSortString(String order, String s) {
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); i++) {
            cnt[s.charAt(i) - 'a']++;
        }
        StringBuilder sb = new StringBuilder(s.length());
        for (int i = 0; i < order.length(); i++) {
            char c = order.charAt(i);
            while (cnt[c - 'a']-- > 0) {
                sb.append(c);
            }
        }
        for (int i = 0; i < 26; i++) {
            while (cnt[i]-- > 0) {
                sb.append((char) ('a' + i));
            }
        }
        return sb.toString();
    }
}

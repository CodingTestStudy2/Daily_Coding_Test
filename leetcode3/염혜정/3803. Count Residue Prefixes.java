// 문자열의 0번째부터 set에 있는지 확인
// 없으면 넣어주고 distinct_cnt + 1
// O(n)

class Solution {
    public int residuePrefixes(String s) {
        Set<Character> set = new HashSet<>();
        int distinct_cnt = 0;
        int result = 0;
        for (int i = 0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (!set.contains(c)) { // 중복이 아니라면
                distinct_cnt++;
                set.add(c);
            }
            int modulo = (i + 1) % 3;
            if (modulo == distinct_cnt) result++;
        }
        return result;
    }
}

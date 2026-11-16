class Solution {
    public String smallestSubsequence(String s) {
        int[] lastIdx = new int[26];
        for (int i = 0; i < s.length(); i++) {
            lastIdx[s.charAt(i)-'a'] = i;
        }

        boolean[] check = new boolean[26];
        Deque<Character> sb = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int idx = c-'a';

            if (check[idx]) continue;

            while (!sb.isEmpty() && sb.peekLast() > c && lastIdx[sb.peekLast() - 'a'] > i) {
                int idx = sb.poll()-'a';
                check[idx] = false;
            }

            sb.addLast(c);
            check[idx] = true;
        }

        StringBuilder ans = new StringBuilder();
        
        for (char c : ans) ans.append(c);

        return ans.toString();
    }
}
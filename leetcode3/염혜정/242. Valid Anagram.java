// o(n)

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] cnt = new int[26];
        for (int i = 0; i<s.length(); i++) {
            int ord = (int) s.charAt(i) - 97;
            cnt[ord]++;
        }

        for (int i = 0; i<t.length(); i++) {
            int ord = (int) t.charAt(i) - 97;
            if (cnt[ord] == 0) return false;
            cnt[ord]--;
        }
        return true;
    }
}

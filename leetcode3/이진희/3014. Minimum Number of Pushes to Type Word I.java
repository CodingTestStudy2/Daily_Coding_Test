class Solution {
    public int minimumPushes(String word) {
        int ans = 0;

        for(int i = 0; i < word.length(); i++) {
            int idx = i / 8;

            ans += idx + 1;
        }

        return ans;
    }
}
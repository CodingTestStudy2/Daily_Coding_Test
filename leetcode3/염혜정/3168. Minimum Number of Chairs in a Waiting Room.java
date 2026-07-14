class Solution {
    public int minimumChairs(String s) {
        int chair = 0;
        int max = 0;
        for (int i = 0; i<s.length(); i++) {
            if (s.charAt(i) == 'E') {
                chair++;
                max = Math.max(max, chair);
            }
            else if (s.charAt(i) == 'L') chair--;
        }
        return max;
    }
}

// O(n)

class Solution {
    public int minRotations(String s) {
        s = "0" + s;
        int rotation = 0;
        for (int i = 0; i<s.length()-1; i++) {
            int from = s.charAt(i) - '0';
            int to = s.charAt(i+1) - '0';

            int right = Math.abs(to - from);
            int left = 10-Math.max(to, from) + Math.min(to, from);
            rotation += right<left? right: left;
        }
        return rotation;
    }
}

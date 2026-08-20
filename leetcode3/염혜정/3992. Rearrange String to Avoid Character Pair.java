// O(n)

class Solution {
    public String rearrangeString(String s, char x, char y) {
        StringBuilder left = new StringBuilder();
        StringBuilder mid = new StringBuilder();
        StringBuilder right = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (c == y) left.append(c);
            else if (c == x) right.append(c);
            else mid.append(c);
        }
        return left.toString() + mid.toString() + right.toString();
    }
}

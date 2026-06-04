class Solution {
    public static void main(String[] args) {
        String aeiou = "aeiou";

        int index = s.length() - 1;
        while (index >= 0 && aeiou.indexOf(s.charAt(index)) >= 0) {
            index--;
        }

        return s.substring(0, index + 1);
    }
}
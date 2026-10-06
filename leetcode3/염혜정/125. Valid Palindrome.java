// 투포인터
// O(n)

class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i<s.length(); i++) {
            char c = Character.toLowerCase(s.charAt(i));
            if (isLetter(c) || isNumber(c)) sb.append(c);
        }
        
        int left = 0;
        int right = sb.length() -1;
        while (left<right) {
            if (sb.charAt(left) != sb.charAt(right)) return false;
            left++;
            right--;
        }
        return true;
    }

    boolean isLetter(int ord) {
        return ord>=97 && ord <=122;
    }

    boolean isNumber(int ord) {
        return ord>=48 && ord <=57;
    }
}

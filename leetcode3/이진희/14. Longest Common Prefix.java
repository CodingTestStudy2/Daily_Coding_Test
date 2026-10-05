class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder sb = new StringBuilder();

        String base = strs[0];

        for(int i=0; i<base.length(); i++) {
            char c = base.charAt(i);
            for(int j=1; j<strs.length; j++) {
                if((strs[j].length()-1)<i || strs[j].charAt(i) != c) {
                    return sb.toString();
                }
            }
            sb.append(c);
        }

        return sb.toString();
    }
}
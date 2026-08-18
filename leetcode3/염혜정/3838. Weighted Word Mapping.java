// 97 ~ 122

class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            int sum = 0;
            for (char c : word.toCharArray()) {
                int num = (int) c - 97;
                sum += weights[num];
            }
            int mod = sum % 26;
            sb.append((char)('z' - mod));
        }
        return sb.toString();
    }
}

class Solution {
    public boolean scoreBalance(String s) {
        int totalSum = 0;
        
        for (char c : s.toCharArray()) {
            totalSum += (c - 'a' + 1);
        }
        
        int prefixSum = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            prefixSum += (s.charAt(i) - 'a' + 1);
            
            if (prefixSum == totalSum - prefixSum) {
                return true;
            }
        }
        
        return false;
    }
}

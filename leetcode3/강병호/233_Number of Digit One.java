class Solution {
    public int countDigitOne(int n) {
        int count = 0;
        long factor = 1; 

        while (factor <= n) {
            long divider = factor * 10;
            long higher = n / divider;
            long current = (n / factor) % 10;
            long lower = n % factor;
            
            if (current == 0) {
                count += higher * factor;
            } else if (current == 1) {
                count += (higher * factor) + (lower + 1);
            } else {
                count += (higher + 1) * factor;
            }
            
            if (n / 10 < factor) break; 
            factor *= 10;
        }
        
        return count;
    }
}
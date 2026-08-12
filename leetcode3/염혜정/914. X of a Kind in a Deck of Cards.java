// O(nlogn)

import java.util.Arrays;

class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        Arrays.sort(deck);

        int g = 0;             
        int count = 1;          
        for (int i = 1; i <= deck.length; i++) {
            if (i < deck.length && deck[i] == deck[i - 1]) {
                count++;        
            } else {
                g = gcd(g, count);  
                count = 1;
            }
        }
        return g >= 2;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minimumLengthEncoding(String[] words) {
        Set<String> goodWords = new HashSet<>(Arrays.asList(words));
        
        for (String word : words) {
            for (int k = 1; k < word.length(); ++k) {
                goodWords.remove(word.substring(k));
            }
        }
        
        int totalLength = 0;
        for (String word : goodWords) {
            totalLength += word.length() + 1;
        }
        
        return totalLength;
    }
}
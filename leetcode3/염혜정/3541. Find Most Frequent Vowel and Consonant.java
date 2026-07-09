// a ~ z 빈도 개수 배열을 구한 뒤 해당 배열에서 각각의 최대값을 구한다.
// O(n)

import java.util.*;

class Solution {
    public int maxFreqSum(String s) {
        int[] alphabet = new int[26];
        for (int i = 0; i<s.length(); i++) {
            int num = (int)s.charAt(i) - 'a';
            alphabet[num]++;
        }
        String vowel = "aeiou";
        int vowelMax = 0;
        for (char c : vowel.toCharArray()) {
            vowelMax = Math.max(vowelMax, alphabet[c - 'a']);
        }
        
        String consonant = "bcdfghjklmnpqrstvwxyz";
        int consonantMax = 0;
        for (char c : consonant.toCharArray()) {
            consonantMax = Math.max(consonantMax, alphabet[c - 'a']);
        }
        return vowelMax + consonantMax;
    }
}

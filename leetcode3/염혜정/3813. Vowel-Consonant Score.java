// 97 ~ 122
// o(n)

class Solution {
    public int vowelConsonantScore(String s) {
        Set<Character> vowels = new HashSet<>(List.of('a', 'e', 'i', 'o', 'u'));

        int v = 0;
        int c = 0;
        for (char letter : s.toCharArray()) {
            int askii = (int) letter;
            if (askii < 97 || askii > 122) continue;

            if (vowels.contains(letter)) v++;
            else c++;
        }
        if (c==0) return 0;
        return v / c;
    }
}

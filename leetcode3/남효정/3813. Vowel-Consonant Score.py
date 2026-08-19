class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for vowel in vowels:
            v += s.count(vowel)
        return v // (len(s) - v)
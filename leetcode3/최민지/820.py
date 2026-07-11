class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)

        for word in list(words):
            for i in range(1, len(word)):
                words.discard(word[i:])

        ans = 0

        for word in words:
            ans += len(word) + 1

        return ans
        
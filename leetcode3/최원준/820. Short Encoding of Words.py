class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(set(words), key=lambda word: word[::-1])

        answer = 0

        for i, word in enumerate(words):
            if i + 1 < len(words) and words[i + 1].endswith(word):
                continue

            answer += len(word) + 1

        return answer

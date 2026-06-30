class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        i = 0
        for p in patterns:
            if p in word:
                i += 1
        return i

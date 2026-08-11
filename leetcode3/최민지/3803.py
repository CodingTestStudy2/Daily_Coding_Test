class Solution:
    def residuePrefixes(self, s: str) -> int:
        result = 0

        for i in range(1, len(s) + 1):
            prefix = s[:i]

            if len(set(prefix)) == len(prefix) % 3:
                result += 1
        
        return result

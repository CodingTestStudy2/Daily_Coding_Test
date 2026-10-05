class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_length = min([len(string) for string in strs])
        n = len(strs)
        
        ans = ""
        for i in range(min_length):
            base_char = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != base_char:
                    return ans
            ans += base_char
        return ans

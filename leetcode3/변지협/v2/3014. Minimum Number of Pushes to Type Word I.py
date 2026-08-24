class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        
        lst = []
        for i in range(26):
            q = i // 8
            lst.append(q+1)
        
        # print(lst)

        return sum(lst[:n])
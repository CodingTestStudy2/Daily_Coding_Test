class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        freq_num = [[freq, num] for num, freq in counter.items()]
        freq_num.sort()
        
        ans = 0
        counter = 0

        while freq_num:
            freq, num = freq_num.pop()
            cost = counter // 8 + 1
            counter+=1
            ans+=cost * freq
        return ans

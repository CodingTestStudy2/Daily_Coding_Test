class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        cnt = Counter(str(n))

        ans = -1
        freq = float("inf")

        for d, c in cnt.items():
            d = int(d)
            if c < freq or (c == freq and d < ans):
                freq = c
                ans = d

        return ans
        
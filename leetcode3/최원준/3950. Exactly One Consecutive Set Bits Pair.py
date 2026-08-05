class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        binary = bin(n)[2:]
        ans = True
        count = 0
        pairs = 0
        for b in binary:
            if b == "1":
                count+=1

                if count >= 2:
                    pairs += 1
            else:
                count = 0
        return pairs == 1

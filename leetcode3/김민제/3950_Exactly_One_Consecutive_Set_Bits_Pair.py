class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        count = 0
        binary = bin(n)[2:]

        for i in range(len(binary)-1):
            if binary[i:i+2] == "11":
                count += 1
        return count == 1     

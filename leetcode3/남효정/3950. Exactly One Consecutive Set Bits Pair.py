class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        binary_str = bin(n)[2:]
        
        count = 0
        
        for i in range(len(binary_str) - 1):
            if binary_str[i] == '1' and binary_str[i+1] == '1':
                count += 1
                
        return count == 1
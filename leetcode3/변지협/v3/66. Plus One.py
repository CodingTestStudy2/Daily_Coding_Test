class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        tmp = ''
        for digit in digits:
            tmp += str(digit)
        
        tmp = str(int(tmp) +1)
        return [int(i) for i in tmp]

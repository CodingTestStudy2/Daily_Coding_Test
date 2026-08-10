class Solution:
    def findComplement(self, num: int) -> int:
        b = format(num, 'b')
        change = ''
        for i in b:
            if i == '0':
                change += '1'
            else:
                change += '0'
        result = int(change, 2)

        return result
    
        
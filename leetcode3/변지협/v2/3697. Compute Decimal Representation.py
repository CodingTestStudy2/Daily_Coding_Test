class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        strn = str(n)[::-1]
        n = len(strn)
        
        lst = []
        m = ''
        for i in range(n):
            lst.append(strn[i] + m)
            m+= '0'
        
        # print(lst)

        lst = [int(i) for i in lst]
        lst = [i for i in lst if i != 0]
        # print(lst)
        return lst[::-1]
        
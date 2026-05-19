#

'''
1. 아이디어 :


2. 시간복잡도 :
    O()

3. 자료구조/알고리즘 :


'''


class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return str(n)[0]!=str(x) and Counter(str(n))[str(x)]>=1

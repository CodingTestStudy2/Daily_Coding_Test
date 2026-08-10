
'''
1. 아이디어 :
이진수 구하고 1을 0으로, 0을 1로 바꾼 후 다시 정수로 변환한다.

2. 시간복잡도 :
o(n)

3. 자료구조/알고리즘 :
'''

class Solution(object):
    def getBinary(self, n):
        s = ''
        while True:
            if n == 0:
                break
            tmp = n % 2
            n = n // 2
            s += str(tmp)

        return s[::-1]

    def getInt(self, b):
        num = 0
        b = b[::-1]
        n = len(b)
        # print(b)
        for i in range(n):
            if int(b[i]) %2 != 0:
                num +=2 ** i

        return num

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # print(self.getBinary(num))
        b = self.getBinary(num)
        tmp = ''
        for i in b:
            tmp += '0' if i == '1' else '1'

        return self.getInt(tmp)        
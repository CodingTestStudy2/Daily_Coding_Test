
'''
1. 아이디어 :

2. 시간복잡도 :
    o(n)

3. 자료구조/알고리즘 :
나머지 연산자를 이용하여 2진수로 변환 후, 1이 연속으로 나오는 경우를 체크하였다.
'''

"""
6 // 2 = 3
6 % 2 == 0
3 // 2 = 1
3 % 2 = 1
1 // 2 = 0
1 % 2 = 1

5 // 2 = 2
5 % 2 = 1
2 // 2 = 1
2 % 2 = 0
1 // 2 = 1
1 % 2 = 1
"""
class Solution(object):
    def consecutiveSetBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bit2 = ''
        tmp = n
        while True:
            if tmp == 0:
                break
            bit2 += str(tmp % 2)
            tmp = tmp // 2

        print(bit2)

        tmp = ''
        ans = 0
        for b in bit2:
            if b == '1' and tmp == '1':
                ans +=1
            tmp = b

        return True if ans == 1 else False
            

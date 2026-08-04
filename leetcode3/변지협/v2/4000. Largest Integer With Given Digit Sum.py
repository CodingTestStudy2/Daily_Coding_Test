
'''
1. 아이디어 :

2. 시간복잡도 :
    o(n^2)

3. 자료구조/알고리즘 :
완전탐색 형태로 문제를 풀었다.
'''

class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        tmp = -1
        # print(10**n)
        for i in range(10**n):
            _sum = 0
            for j in str(i):
                _sum += int(j)

            # print('i,_sum:',i,_sum)
            
            if _sum == s:
                if tmp < i:
                    tmp = i

        return tmp    
            
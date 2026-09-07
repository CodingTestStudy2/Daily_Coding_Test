
'''
1. 아이디어 :
k진수로 변환하고, 각 자리수를 더한다.

2. 시간복잡도 :
o(log n)

3. 자료구조/알고리즘 :
'''
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        s = ''
        while True:
            if n == 0:
                break
            r = n % k
            n = n // k
            s += str(r)
        
        print(s)

        return sum([int(i) for i in s])
            
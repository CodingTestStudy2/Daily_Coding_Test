#

'''
1. 아이디어 :
예시를 보고 시도해봤다가...
분석해보면
sum_odd = n*n
sum_even = n(n+1)
gcd(n*n, n(n+1)) -> n * gcd(n, n+1) -> n * 1

2. 시간복잡도 :
    O(1)

3. 자료구조/알고리즘 :
gcd

'''

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n

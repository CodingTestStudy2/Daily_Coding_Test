#

'''
1. 아이디어 :
b가 a에 포함되려면 a+(a*x)가 b의 길이보다 크거나, a+(a*x)+1이 b의 길이보다 커야한다.
두 가지 string을 만들어놓고 b가 a에 포함되는지 확인

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        rep = 1
        a_string = a

        while len(a_string) < len(b):
            a_string += a
            rep += 1

        if b in a_string:
            return rep

        a_string+=a
        rep += 1

        if b in a_string:
            return rep

        return -1

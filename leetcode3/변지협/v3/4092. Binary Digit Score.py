'''
1. 아이디어 :
2. 시간복잡도 :
O(bin(a) + bin(b))
3. 자료구조/알고리즘 :
'''
class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        a = len([i for i in bin(a) if i == str(1)])
        b = len([i for i in bin(b) if i == str(1)])

        print(a,b)

        if a >= b:
            return a * b
        else:
            return int(b / a)

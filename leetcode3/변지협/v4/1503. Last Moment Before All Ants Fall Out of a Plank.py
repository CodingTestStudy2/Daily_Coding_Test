'''
1. 아이디어 :
생각해보면 개미가 떨어질 수 있는게 처음 배치에따라 달라지지 않음.
충돌을해도 총 간 거리는 유지됨.

2. 시간복잡도 :
o(1)

3. 자료구조/알고리즘 :
'''

class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        if not left:
            left.append(0)
        if not right:
            right.append(n)
        return max([abs(n-min(right)), abs(max(left))])
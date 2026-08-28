
'''
1. 아이디어 :
생각해보면 x좌표와 y좌표의 차이가 모두 짝수이거나 모두 홀수이면 도달 가능하다.

2. 시간복잡도 :
o(1)

3. 자료구조/알고리즘 :
'''
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        x,y = start
        tx,ty = target

        if abs(x - tx) % 2 == abs(y - ty) % 2:
            return True
        else:
            return False
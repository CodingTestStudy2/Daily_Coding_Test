#

'''
1. 아이디어 :
두 사각형이 겹치는지 확인합니다.
- 겹치는 경우: 두 사각형 영역의 합
- 겹치지 않는 경우: 4개의 가로, 세로 좌표들을 정렬한 후, 가운데 두개의 좌표들이 겹치는 좌표이므로,
                   두 사각형 영엽의 합 - 겹치는 영역

2. 시간복잡도 :
    O(4log4)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        is_collide = True
        if ax1 > bx2:
            is_collide = False
        elif bx1 > ax2:
            is_collide = False
        elif ay1 > by2:
            is_collide = False
        elif by1 > ay2:
            is_collide = False

        collide = 0
        if is_collide:
            x = [ax1, ax2, bx1, bx2]
            y = [ay1, ay2, by1, by2]
            x.sort()
            y.sort()
            collide = abs(x[1]-x[2]) * abs(y[1]-y[2])

        return abs(ax1-ax2) * abs(ay1-ay2) + abs(bx1-bx2) * abs(by1-by2) - collide

        
            

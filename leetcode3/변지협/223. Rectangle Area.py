'''
1. 아이디어 :
    두 직사각형 합 - 겹치는 직사각형
2. 시간복잡도 :
    O(1)
3. 자료구조/알고리즘 :
'''

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        cx1 = max(ax1,bx1)
        cx2 = min(ax2,bx2)
        cy1 = max(ay1,by1)
        cy2 = min(ay2,by2)

        ans = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        if cx2 - cx1 > 0 and cy2 - cy1 > 0:
            ans -= (cx2 - cx1) * (cy2 - cy1)
        
        return ans
'''
실패
'''

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        st = set()
        for x in range(x1,x2+1):
            st.add((x,y1))
            st.add((x,y2))
        for y in range(y1,y2+1):
            st.add((x1,y))
            st.add((x2,y))
        
        while st:
            x,y = st.pop()
            if ((x-xCenter) ** 2 + (y-yCenter) ** 2) ** 0.5 <= radius:
                return True
        
        return False

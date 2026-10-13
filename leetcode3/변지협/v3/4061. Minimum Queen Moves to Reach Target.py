'''
1. 아이디어 :
따져봤을 때 2번 안에 퀸이 다 갈 수 있음.
0번: src == target
1번: 퀸의 이동경로 (src!=target)
2번: 나머지 전부

2. 시간복잡도 :
o(1) - 경로만 바로 구하면 됨

3. 자료구조/알고리즘 :
'''
from collections import deque
class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        x1,y1 = tuple(source)
        x2,y2 = tuple(target)
        if x1 == x2 and y1 == y2:
            return 0
        
        st = set()

        for i in range(1,9):
            st.add((x1,i))
            st.add((i,y1))
        
        print(st)

        x = x1
        y = y1
        while 1 <= x < 9 and 1<= y < 9:
            xtmp = x+1
            ytmp = y+1
            x = xtmp
            y = ytmp
            st.add((x,y))

        x = x1
        y = y1
        while 1 <= x < 9 and 1<= y < 9:
            xtmp = x-1
            ytmp = y-1
            x = xtmp
            y = ytmp
            st.add((x,y))
        x = x1
        y = y1
        
        while 1 <= x < 9 and 1<= y < 9:
            xtmp = x+1
            ytmp = y-1
            x = xtmp
            y = ytmp
            st.add((x,y))
        x = x1
        y = y1

        while 1 <= x < 9 and 1<= y < 9:
            xtmp = x-1
            ytmp = y+1
            x = xtmp
            y = ytmp
            st.add((x,y))
        
        if (x2,y2) in st:
            return 1
        else:
            return 2        
            

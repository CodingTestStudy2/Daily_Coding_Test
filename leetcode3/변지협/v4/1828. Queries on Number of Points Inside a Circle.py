'''
1. 아이디어 :
원과 가까운지 체크

2. 시간복잡도 :
o(n*m) (정렬)

3. 자료구조/알고리즘 :
'''

class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        lst = []
        for x1,y1,r in queries:
            tmp = 0
            for x2,y2 in points:
                if (x2 - x1)**2 + (y2 - y1)**2 <= r**2:
                    # print(x1,y1,x2,y2,r,(x2 - x1)^2 + (y2 - y1)^2)
                    tmp += 1
            lst.append(tmp)
        return lst
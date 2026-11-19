#

'''
1. 아이디어 :
완전 탐색으로 쿼리마다 점들의 거리를 계산한다.

2. 시간복잡도 :
    O(n * m)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        
        def get_distance(x1, y1, x2, y2):
            return (abs(x1-x2) ** 2 + abs(y1-y2) ** 2) ** (1/2)
        
        ans = []

        for x1, y1, r in queries:
            count = 0
            for x2, y2 in points:
                if get_distance(x1, y1, x2, y2) <= r:
                    count += 1
            ans.append(count)
        return ans

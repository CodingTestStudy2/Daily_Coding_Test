#

'''
1. 아이디어 :
기준 포인트와 나머지 포인트들의 거리를 구하고 카운트를 한다.
카운트된 갯수(m)중 2개씩 조합한다 m * (m-1)

2. 시간복잡도 :
    O(n * n)

3. 자료구조/알고리즘 :
hashmap

'''
class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        
        def get_distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return (x1-x2)**2 + abs(y1-y2)**2
        
        n = len(points)
        # distances = [[0 for _ in range(n)] for _ in range(n)]

        # for row in range(n):
        #     for col in range(n):
        #         if row == col: continue
        #         distances[row][col] = get_distance(points[row], points[col])

        # for a in distances:
        #     print(a)

        ans = 0
        for mid in points:
            distances = defaultdict(int)

            for point in points:
                if mid == point:
                    continue
                
                distance = get_distance(mid, point)
                distances[distance] += 1
            
            for _, count in distances.items():
                ans += count * (count-1)
        return ans

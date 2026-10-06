'''
1. 아이디어 :
- 각 점을 기준으로 다른 점들과의 거리를 계산하고, 같은 거리를 가진 점들의 개수를 세어 부메랑의 수를 계산.
- 이거 원래 3중 for문 돌았는데 그러면 시간초과난다.
2. 시간복잡도 :
o(n^2)
3. 자료구조/알고리즘 :
'''

from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        n = len(points)
        if n < 3:
            return 0

        ans = 0
        for i in range(n):
            dic = defaultdict(int)
            for j in range(n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                dic[(x2-x1)** 2 + (y2-y1)**2] += 1
            # print(dic)
            for value in dic.values():
                if value >= 2:
                    ans += value * (value -1)
                
        
        return ans
                    
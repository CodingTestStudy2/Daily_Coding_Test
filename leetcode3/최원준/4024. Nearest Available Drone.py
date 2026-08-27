#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        
        def get_manhattan_distance(x1, y1, x2, y2):
            return abs(x1-x2) + abs(y1-y2) #|xi - xj| + |yi - yj|

        min_distance = float('inf')
        ans = -1

        for i in range(len(drones)):
            x, y, distance = drones[i]
            m_distance = get_manhattan_distance(x, y, target[0], target[1])
            if m_distance < min_distance and m_distance<=distance:
                min_distance = m_distance
                ans = i
        return ans

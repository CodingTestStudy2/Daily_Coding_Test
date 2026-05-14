#

'''
1. 아이디어 :
도착지점에 유령이 나보다 먼저 도착한다면 무조건 잡힙니다.
(도착지첨과 나의 거리)가 모든 (도착지점과 유령 거리)보다 클때만 잡히지 않습니다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_distance = self.calculate_distance([0,0], target)
        for ghost in ghosts:
            distance = self.calculate_distance(ghost, target)
            if distance <= my_distance:
                return False
        return True

    def calculate_distance(self, start: List[int], dest: List[int]) -> int:
        return abs(start[0]-dest[0]) + abs(start[1]-dest[1])
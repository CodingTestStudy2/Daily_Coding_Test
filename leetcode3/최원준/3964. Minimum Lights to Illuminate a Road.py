#

'''
1. 아이디어 :
왼쪽에서 순회, 오른쪽에서 순회하면서 불이 켜져있는 곳들을 체크합니다.
불이 꺼져 있는 곳(i)들에 대해 i+1에 불을 켜서 최대로 불을 키게(i, i+1, i+2)합니다.

2. 시간복잡도 :
    O(n + n + n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        lit = [0] * n

        distance = 0
        for i in range(n):
            distance = max(distance-1, lights[i] +1 if lights[i] > 0 else 0)
            if distance > 0:
                lit[i] = 1

        distance = 0
        for i in range(n-1, -1, -1):
            distance = max(distance-1, lights[i] +1 if lights[i] > 0 else 0)
            if distance > 0:
                lit[i] = 1
        
        # print(lit)

        ans = 0
        for i in range(n):
            if lit[i] != 0:
                continue

            pos = min(i+1, n-1)
            for j in range(max(0, pos-1), min(n, pos+2)):
                lit[j] = 2
            ans+=1
        # print(lit)
        return ans
                    

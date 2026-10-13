#

'''
1. 아이디어 :
미리 trip마다 탑승, 내리는 인원들을 구합니다.

2. 시간복잡도 :
    O(n+n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        n = len(trips)
        boarding = [0] * 1001
        curr = 0
        
        for passengers, start, end in trips:
            boarding[start] += passengers
            boarding[end] -= passengers
        
        for i in range(1000):
            curr += boarding[i]
            if curr > capacity:
                return False

        return True

        
            
            

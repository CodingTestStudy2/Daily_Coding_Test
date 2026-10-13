'''
1. 아이디어 :
1943. Describe the Painting.py
4개월전에 코딩테스트 참여했을 때 풀었던 문제인데 구조적으로 100% 동일한 문제임.
from을 +, to를 -로 둬서 해시의 누적합을 구하고, 여기서 누적합이 capacity를 초과하는지 확인하면 된다.

2. 시간복잡도 :
o(n)

3. 자료구조/알고리즘 :
- 배열(누적합), 해시맵(탑승/하차 위치 기록)
'''
from collections import defaultdict
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        dic = defaultdict(int)
        
        for n, _from, to in trips:
            dic[_from] += n
            dic[to] -= n
        
        print(dic)

        current = 0
        for i in [value for key, value in sorted(dic.items(), key=lambda x:x[0])]:
            current += i
            if current > capacity:
                return False
        
        return True

                

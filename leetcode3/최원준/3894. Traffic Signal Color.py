#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(1)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def trafficSignal(self, timer: int) -> str:
        return "Red" if 30<timer<=90 else "Orange" if timer == 30 else "Green" if timer == 0 else "Invalid"

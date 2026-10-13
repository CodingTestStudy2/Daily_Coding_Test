#

'''
1. 아이디어 :
최대 2번 움직입니다
0번: 같은 점
1번: 같은 가로/세로/대각
2번: 위 제외 나머지

2. 시간복잡도 :
    O(1)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        s1, s2 = source
        e1, e2 = target
        
        if s1 == e1 and s2 ==e2:
            return 0
        if s1 == e1 or s2 == e2 or abs(s1-e1) == abs(s2-e2):
            return 1
        return 2
        
        

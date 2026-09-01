
'''
1. 아이디어 :
따지고 보면 먼저 돌을 가져가는 사람이 항상 이길 것이라고 생각이 들었음.
선공이 짝수번째만 가져간다고 생각하면 짝수만 가져갈 수 있음. 홀수만 가져간다고 하면 홀수만 가져갈 수 있음.
return True 하니까 답이라고 한다.

2. 시간복잡도 :
o(1)

3. 자료구조/알고리즘 :
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
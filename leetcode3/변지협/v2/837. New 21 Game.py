'''
1. 아이디어 :
randint로 그냥 다 구하려고 했으나 시간초과 발생

2. 시간복잡도 :

3. 자료구조/알고리즘 :
'''
from random import randint

class Solution:
    def playGame(self, k, maxPts):
        _sum = 0
        while True:
            _sum += randint(1,maxPts)
            if _sum >= k:
                return _sum

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        plays = []
        length = 500000

        for i in range(length):
            plays.append(self.playGame(k,maxPts))

        # print(plays)
        
        plays = [i for i in plays if i <= n]
        return len(plays) / length
        
#

'''
1. 아이디어 :
나올 수 있는 모든 조합을 구하지만(backtrack), 반복 계산을 줄이기 위해 memoization 적용
한번 계산한 조합을 다시 계산하지 않도록 memo에 combination의 결과값을 저장하고 꺼내씁니다.
숫자를 쓰지 않았으면, 해당 숫자를 쓰고, 상대방이 남는 값으로 이길 수 있는지 판단을 통해 결과를 얻음

2. 시간복잡도 :
    O(2**M * M**2)

3. 자료구조/알고리즘 :
backtrack, memoization

'''

from collections import deque
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        total = sum(num for num in range(1, maxChoosableInteger+1))
        if total < desiredTotal:
            return False
        if maxChoosableInteger >= desiredTotal:
            return True

        used = [False] * (maxChoosableInteger + 1)
        memo = {}

        def backtrack(remain) -> bool:
            combination = tuple(used)

            if combination in memo:
                return memo[combination]

            for i in range(1, maxChoosableInteger + 1):
                if used[i]:
                    continue
                
                if i>=remain: # win
                    memo[combination] = True
                    return True
                
                used[i] = True
                opponent_win = backtrack(remain-i)
                used[i] = False

                if not opponent_win:
                    memo[combination] = True
                    return True
            
            memo[combination] = False
            return False #lose
        
        return backtrack(desiredTotal)

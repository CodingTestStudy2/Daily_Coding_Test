'''
실패 (시간초과)

1. 아이디어 :
모든 순열을 다 만들어서, 그 순서대로 태스크를 세션에 차례로 담아보는 완전탐색.
현재 세션에 담을 수 없으면 새 세션을 열고, 마지막에 세션 개수를 세어 최솟값 갱신.

2. 시간복잡도 :
o(n!) — 순열 개수가 n! 이고 각 순열을 o(n)에 훑으므로 n*n!.
n=14 이면 14! ≈ 8.7 * 10^10 이라 시간초과.

3. 자료구조/알고리즘 :
순열 (itertools.permutations), 완전탐색, 그리디 채우기
(정답은 비트마스크 dp / 백트래킹으로 접근해야 함)

'''

from itertools import permutations
class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        n = len(tasks)
        perm = permutations(tasks,n)
        # print(list(perm))

        ans = 10e9
        for tp in perm:
            _sum = 0
            curr_session = 0
            for i in list(tp):
                if curr_session + i > sessionTime:
                    curr_session = 0
                    _sum += 1
                curr_session += i

            if curr_session > sessionTime:
                _sum += 1
            
            ans = min(ans,_sum)

        return ans + 1

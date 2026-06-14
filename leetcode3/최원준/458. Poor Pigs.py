#

'''
1. 아이디어 :
    - 총 실험 가능 횟수는 minutesToTest // minutesToDie 이다.
    - 돼지 1마리는 "1번째 실험 후 죽음, 2번째 실험 후 죽음, ..., 끝까지 생존"으로
      총 rounds + 1개의 상태를 표현할 수 있다.
    - 돼지가 pigs마리라면 표현 가능한 경우의 수는 (rounds + 1) ** pigs 이다.
    - 이 값이 buckets 이상이 되는 최소 pigs를 찾는다.

2. 시간복잡도 :
    O(log_{rounds+1}(buckets))

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie
        states = rounds + 1

        pigs = 0
        capacity = 1

        while capacity < buckets:
            pigs += 1
            capacity *= states
        return pigs

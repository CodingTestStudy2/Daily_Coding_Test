'''
1. 아이디어 :
각 숫자에서 나이트가 한 번에 이동할 수 있는 다음 숫자들을 인접 리스트(mapping)로 미리 정의한다.
dp[숫자] = 해당 숫자에서 끝나는 길이 i짜리 번호의 개수 로 두고,
매 단계마다 모든 숫자에서 갈 수 있는 다음 숫자에 현재 값을 더해 누적한다.
n-1번 반복한 뒤 모든 숫자의 값을 합하고 10^9+7로 나눈 나머지를 반환한다.

2. 시간복잡도 :
o(n) - 매 단계 상수 개(최대 3개)의 간선만 확인

3. 자료구조/알고리즘 :
DP, 해시맵(그래프 인접 리스트)

'''

class Solution:
    def knightDialer(self, n: int) -> int:
        dic = {}
        mod = 10 ** 9 + 7
        for i in range(10):
            dic[i] = 1

        mapping = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [0,3,9],
            5: [],
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9: [2,4]
        }

        for i in range(1,n):
            tmp = {}
            for i in range(10):
                tmp[i] = 0
            for key, value in dic.items():
                for _next in mapping[key]:
                    tmp[_next] += value % mod
            dic = tmp

        return sum([value for value in dic.values()]) % mod

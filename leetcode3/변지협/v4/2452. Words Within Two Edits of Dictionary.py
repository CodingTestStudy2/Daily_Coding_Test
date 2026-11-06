'''
1. 아이디어 :
각 query마다 dictionary의 단어들과 같은 위치의 문자를 비교해서
서로 다른 문자의 개수가 2개 이하인 단어가 하나라도 있으면 정답에 추가한다.

2. 시간복잡도 :
o(len(queries) * len(dictionary) * len(query))

3. 자료구조/알고리즘 :
문자열 완전탐색(브루트포스)

'''

class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        ans = []

        for query in queries:
            n = len(query)
            breaker=False
            for word in dictionary:
                not_same = 0
                for i in range(n):
                    if word[i] != query[i]:
                        not_same += 1

                if not_same <= 2:
                    breaker = True
                    ans.append(query)
                    break
                if breaker:
                    break

        return ans

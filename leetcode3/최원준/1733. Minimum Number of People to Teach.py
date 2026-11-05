#

'''
1. 아이디어 :
서로 소통할 수 없는 사람들을 모아둡니다.
그 사람들 중, 가장 많이 알고 있는 언어를 나머지 사람들에게 가르치면 됩니다.

2. 시간복잡도 :
    O(n*m + k + n*n)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        m = len(languages)
        k = len(friendships)
        language_sets = [set(language) for language in languages]

        users = set()

        for a, b in friendships:
            a_set = language_sets[a-1]
            b_set = language_sets[b-1]

            if a_set & b_set:
                continue # can communicate
            
            users.add(a-1)
            users.add(b-1)
        
        ans = len(users)

        for language in range(1, n+1):
            count = 0

            for user in users:
                if language not in language_sets[user]:
                    count += 1
            
            ans = min(ans, count)
        return ans

'''
1. 아이디어 :
- 나이가 120까지 있으니, 나이별로 묶어서 한번에 계산하는 방법

2. 시간복잡도 :
    O(n*n)

3. 자료구조/알고리즘 :
해시맵

'''

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = Counter(ages)
        ans = 0

        for x in count:
            for y in count:
                if self.can_send(x, y):
                    if x == y:
                        ans += count[x] * (count[x] - 1)
                    else:
                        ans += count[x] * count[y]

        return ans

    def can_send(self, x: int, y: int) -> bool:
        if y <= 0.5 * x + 7:
            return False
        if y > x:
            return False
        if y > 100 and x < 100:
            return False
        return True

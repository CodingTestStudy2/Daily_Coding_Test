#

'''
1. 아이디어 :
같은 숫자들의 인덱스를 모아놓고, 3개 이상의 인덱스가 채워질때마다 뒤에 3개씩 연산을 합니다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
해시맵 / -

'''


from collections import defaultdict
class Solution:

    def __init__(self):
        self._ans = float('inf')

    def minimumDistance(self, nums: List[int]) -> int:
        candids = defaultdict(list)
        for i, num in enumerate(nums):
            candids[num].append(i)

            if len(candids[num]) >=3:
                alist = candids[num]
                self._ans = min(self._ans, self.get_sum(alist[-1], alist[-2], alist[-3]))

        return -1 if self._ans == float('inf') else self._ans

    def get_sum(self, num1, num2, num3) -> int:
        return abs(num1-num2) + abs(num2-num3) + abs(num3-num1)
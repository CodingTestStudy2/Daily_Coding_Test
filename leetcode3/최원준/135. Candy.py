#

'''
Approach1:
1. 아이디어 :
- 작은 숫자부터 채운다.
- 숫자들의 인덱스들을 저장한다.
- 작은 숫자들을 순회하면서 양쪽 rating 값과, candy 값을 바탕으로 최소 candy 값을 구한다.

2. 시간복잡도 :
    O(n + n + nlogn + n + n)

3. 자료구조/알고리즘 :
해시맵, 해시셋 

Approach2:
1. 아이디어 :
- 왼쪽에서 한번, 오른쪽에서 한번 계산한다.

2. 시간복잡도 :
    O(n + n + n + n)

3. 자료구조/알고리즘 :
-

'''

from collections import defaultdict
from typing import List

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [0] * n
        indexes = defaultdict(list)

        for i, rating in enumerate(ratings):
            indexes[rating].append(i)

        sorted_ratings = sorted(set(ratings))

        def get_min_candy(rating, index):
            value = 1

            if index - 1 >= 0 and ratings[index - 1] < rating:
                value = max(value, candies[index - 1] + 1)

            if index + 1 < n and ratings[index + 1] < rating:
                value = max(value, candies[index + 1] + 1)

            return value

        for rating in sorted_ratings:
            for index in indexes[rating]:
                candies[index] = get_min_candy(rating, index)

        return sum(candies)

    def candy2(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

"""
1. 아이디어 :
- 매 라운드마다 nums에 남아있는 서로 다른 값들을 하나씩 제거해 오름차순으로 ans에 이어붙인다.
- Counter로 남은 값들의 개수를 세고, 등장하는 key마다 nums에서 하나씩 제거해 tmp에 모은 뒤 정렬해 ans에 extend.
- nums가 빌 때까지 반복.

2. 시간복잡도 :
o(n^2) (최대값의 개수만큼 라운드 반복 * Counter/remove 비용)

3. 자료구조/알고리즘 :
해시맵(Counter), 정렬, 시뮬레이션

"""

from collections import Counter


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while nums:
            tmp = []
            c = Counter(nums)
            for key in c.keys():
                nums.remove(key)
                tmp.append(key)
            tmp.sort()
            ans.extend(tmp)

        return ans

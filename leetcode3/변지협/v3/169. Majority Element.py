'''
1. 아이디어 :
- Counter로 각 숫자의 등장 횟수를 세고, 횟수 기준 내림차순 정렬했을 때 첫 번째 원소를 반환.
- 과반수 원소는 항상 존재하므로 가장 많이 등장한 값이 정답.
2. 시간복잡도 :
o(n log n)  (Counter는 O(n), 정렬은 O(k log k) ≤ O(n log n))
3. 자료구조/알고리즘 :
해시맵(Counter) + 정렬

'''

from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)[0][0]

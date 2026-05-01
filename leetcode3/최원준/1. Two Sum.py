#

'''
1. 아이디어 :
- 미리 방문한 숫자들을 해시맵에 저장.
- 현재 숫자와 타겟에서 현재 숫자를 뺀 숫자가 해시맵에 존재하는지 확인.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
해시맵

'''

from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = defaultdict(int)
        for i, num in enumerate(nums):
            need = target - num
            if need in cache:
                return [i, cache[need]]
            cache[num] = i
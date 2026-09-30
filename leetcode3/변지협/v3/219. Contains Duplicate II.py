'''
1. 아이디어 :
같은 값을 가진 인덱스들을 값별로 모아 리스트로 저장한 뒤, 각 리스트에서 서로 인접한
인덱스들의 차이가 k 이하인지 확인한다.

2. 시간복잡도 :
o(n)

3. 자료구조/알고리즘 :
해시맵(defaultdict(list))
'''
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = defaultdict(list)
        n = len(nums)
        for i in range(n):
            dic[nums[i]].append(i)

        for key, lst in dic.items():
            m = len(lst)
            if m < 2:
                continue

            last = -1
            while lst:
                elem = lst.pop()
                if last != -1 and abs(elem - last) <= k:
                    return True
                last = elem

        return False

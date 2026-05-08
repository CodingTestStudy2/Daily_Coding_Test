'''
1. 아이디어 :
    같은거 찾아서 딕셔너리에 넣고 최소값 구하기.

2. 시간복잡도 :
    O(n) + O(n)

3. 자료구조/알고리즘 :
'''
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)

        # 0 1 5 10

        _min = 99999

        for key, value in dic.items():
            # print(key, value)

            for i in range(len(value) - 2):
                a = value[i]
                b = value[i+1]
                c = value[i+2]
                abs_sum = abs(a -b) + abs(b-c) + abs(c-a)
                if _min > abs_sum:
                    _min = abs_sum

        return _min if _min != 99999 else -1
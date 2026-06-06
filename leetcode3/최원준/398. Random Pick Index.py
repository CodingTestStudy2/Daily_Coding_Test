#

'''
1. 아이디어 :
같은 확률로 랜덤하게 출력하는 가장 쉬운 방법은 deque를 사용하여 선택될때 맨 앞에서 꺼내고, 다시 맨 뒤에 넣는 방법이 있습니다.

2. 시간복잡도 :
    O(n), O(n)
    
3. 자료구조/알고리즘 :
dict, deque

'''
from collections import deque
class Solution:

    def __init__(self, nums: List[int]):
        self.index = {}
        for i, num in enumerate(nums):
            if num not in self.index:
                self.index[num] = deque()
            self.index[num].append(i)

    def pick(self, target: int) -> int:
        left = self.index[target].popleft()
        self.index[target].append(left)
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

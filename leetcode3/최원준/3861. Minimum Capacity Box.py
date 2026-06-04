#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ans = -1
        smallest = float('inf')

        for i, box in enumerate(capacity):
            if itemSize <= box and smallest > box:
                ans = i
                smallest = box
        return ans

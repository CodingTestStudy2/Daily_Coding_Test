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
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]

        for num in encoded:
            arr.append(arr[-1] ^ num)

        return arr

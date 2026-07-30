#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(len(n) + len(n))

3. 자료구조/알고리즘 :
배열

'''

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp = [c for c in str(n) if c != "0"]
        return 0 if n == 0 else int("".join(temp)) * sum([int(c) for c in temp])
        

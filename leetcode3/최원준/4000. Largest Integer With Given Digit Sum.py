#

'''
1. 아이디어 :
맨앞을 9로 채우면서 s를 차감합니다.

2. 시간복잡도 :
    O(5)

3. 자료구조/알고리즘 :
-

'''
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        ans = 0

        for _ in range(n):
            num = min(9, s)
            ans = ans * 10 + num
            s-=num
        
        return -1 if s>0 else ans

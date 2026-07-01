#

'''
1. 아이디어 :
투포인터를 사용한다.
두 포인터가 겹칠때까지 움직이며 값을 계산한다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
투포인터

'''

class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n-1
        l_val = 0
        r_val = 0

        while left <= right:
            if l_val <= r_val:
                l_val+=ord(s[left])-96
                left+=1
            else:
                r_val+=ord(s[right])-96
                right-=1
        return l_val == r_val
        
            

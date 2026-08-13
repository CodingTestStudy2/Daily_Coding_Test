'''
1. 아이디어 :
arr 뒤집고 pop()할 때는 ans에 안넣음.

2. 시간복잡도 :

3. 자료구조/알고리즘 :
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        lmt = 0
        arr = arr[::-1]
        while True:
            if len(arr) == 0:
                lmt += 1
            elif arr[-1] == i:
                arr.pop()
            else:
                lmt += 1
            
            if lmt == k:
                break
            i += 1

        return i

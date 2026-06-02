#

'''
1. 아이디어 :
범위가 <=100 이라서 100개의 메모리 공간을 가진 배열을 선언.
bulb 마다 on off 기록.

2. 시간복잡도 :
    O(n+n)

3. 자료구조/알고리즘 :
-

'''

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        toggle = [False] * 101
        for bulb in bulbs:
            toggle[bulb] = not toggle[bulb]
        
        ans = []
        for i in range(101):
            if toggle[i]:
                ans.append(i)
        return ans

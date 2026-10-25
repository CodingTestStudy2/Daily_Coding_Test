'''
1. 아이디어 :
- 심는 순서를 바꿀 수 있으므로, growTime이 긴 씨앗을 먼저 심는 게 유리하다 (growTime 내림차순 정렬).
- 정렬된 순서대로 plantTime을 누적해 심는 완료 시점 tmp를 구하고,
  각 씨앗이 피는 날 = tmp + growTime 중 최댓값이 정답.

2. 시간복잡도 :
o(n log n)

3. 자료구조/알고리즘 :
그리디, 정렬
'''

class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        psum = sum(plantTime)
        pairs = sorted(zip(plantTime, growTime), key= lambda x: x[1], reverse=True)

        lst = []
        tmp = 0
        for ptime, gtime in pairs:
            tmp += ptime
            lst.append((tmp, gtime))

        return max([x+y for x,y in lst])

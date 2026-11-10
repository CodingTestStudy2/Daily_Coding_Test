#

'''
1. 아이디어 :
최소 떨어져있는 거리와 최대 떨어져있는 거리를 구합니다. (가장 높은 - 가장 낮은 위치) // m
이분탐색을 통해 거리들을 선정하고,

공을 거리만큼 띄워서 위치시키는게 가능한지 검토합니다.
안된다면 공 사이 거리가 너무 먼거고,
된다면 공 사이 거리가 너무 가깝습니다.

2. 시간복잡도 :
    O(nlogn)

3. 자료구조/알고리즘 :
이분탐색

'''
class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        n = len(position)
        position.sort()

        def is_possible(distance):
            count = 1
            prev = position[0]

            for pos in position[1:]:
                if pos - prev >= distance:
                    count += 1
                    prev = pos

                    if count >= m:
                        return True
            
            return False
        
        left = 1
        right = (position[-1] - position[0]) // (m-1)

        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if is_possible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans

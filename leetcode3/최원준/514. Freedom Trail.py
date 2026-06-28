#

'''
1. 아이디어 :
ring의 각 문자가 등장하는 인덱스들을 미리 저장한다.
현재 ring 위치(pos)와 현재 key 위치(index)를 상태로 두고, dfs(pos, index)가 남은 key를 완성하는 최소 비용을 반환하게 한다.
key[index]가 등장하는 모든 위치(next_pos)를 후보로 보며, 현재 위치에서 해당 위치까지의 최소 회전 거리와 버튼 클릭 1회를 더한다.
같은 상태는 반복될 수 있으므로 메모이제이션으로 저장하고, 모든 후보 중 최소값을 선택한다.

2. 시간복잡도 :
    O(n * m^2) n = key, m = ring

3. 자료구조/알고리즘 :
    dfs, memoization

'''

from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        ring_dict = defaultdict(list)
        ring_list = []

        for i, char in enumerate(ring):
            ring_list.append(char)
            ring_dict[char].append(i)

        # print(ring_list)
        # print(ring_dict)
        

        @lru_cache(None)
        def dfs(pos, index):
            if index == len(key):
                return 0
            
            ans = float('inf')
            target_char = key[index]

            for next_pos in ring_dict[target_char]:
                diff = abs(pos - next_pos)
                rotate_cost = min(diff, n-diff)

                ans = min(
                    ans, rotate_cost + 1 + dfs(next_pos, index + 1)
                )
            return ans
        
        return dfs(0, 0)

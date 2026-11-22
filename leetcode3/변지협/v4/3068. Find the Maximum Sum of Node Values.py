'''
실패 (오답)

1. 아이디어 :
그래프를 BFS로 순회하면서 부모-자식 노드를 한 쌍으로 보고,
(nums[자식] ^ k) + (nums[부모] ^ k) 가 원래 두 수의 합보다 크면
두 노드를 동시에 XOR 연산하는 그리디 접근.

2. 시간복잡도 :
o(n)

3. 자료구조/알고리즘 :
bfs, 인접 리스트, 그리디

'''

from collections import defaultdict, deque


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dic = defaultdict(list)

        for a, b in edges:
            dic[a].append(b)
            dic[b].append(a)

        visited = [False] * n
        dq = deque()
        dq.append(0)
        visited[0] = True

        while dq:
            i = dq.popleft()

            for elem in dic[i]:
                if not visited[elem]:
                    if (nums[elem] ^ k) + (nums[i] ^ k) >= nums[elem] + nums[i]:
                        nums[elem] = nums[elem] ^ k
                        nums[i] = nums[i] ^ k
                    dq.append(elem)
                    visited[elem] = True

        return sum(nums)

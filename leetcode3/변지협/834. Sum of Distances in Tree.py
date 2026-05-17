
'''
1. 아이디어 :
    그냥 전체 탐색하면 시간초과 나옴
    루트노드에서 먼저 정답 구하고 자식 노드로 내려올때마다
    오른쪽으로 가면 왼쪽이 멀어지고 왼쪽으로 가면 오른쪽이 멀어짐 - 이에 대응한 수식 세워서 진행
2. 시간복잡도 :
    O(n)?
3. 자료구조/알고리즘 :
    dfs
'''

from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n
        answer = [0] * n
        
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    answer[node] += answer[child] + count[child]
        
        dfs(0,-1)
        # print(count, answer)

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    answer[child] = answer[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs2(0,-1)
        return answer 
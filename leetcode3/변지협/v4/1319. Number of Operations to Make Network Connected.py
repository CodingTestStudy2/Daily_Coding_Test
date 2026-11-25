'''
1. 아이디어 :
간선(connections)이 n-1개보다 적으면 모든 컴퓨터를 하나로 연결할 수 없으므로 -1.
그 외에는 유니온 파인드로 연결 요소를 합치고, 남은 연결 요소 개수 - 1 만큼
간선을 재배치하면 되므로 (연결 요소 수 - 1) 을 반환한다.

2. 시간복잡도 :
o(n) — union/find 각각 o(n) 최악(경로 압축 없음), 전체 o(n^2) 최악

3. 자료구조/알고리즘 :
union-find (disjoint set), 그래프

'''

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        cn = len(connections)

        if n - 1 > cn:
            return -1

        parents = list(range(n))

        def find(x):
            if parents[x] == x:
                return x
            else:
                return find(parents[x])

        def union(x, y):
            parents[find(y)] = find(x)

        for a, b in connections:
            union(a, b)

        ans = 0
        for i in range(n):
            if i == find(i):
                ans += 1

        return ans - 1

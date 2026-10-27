#

'''
1. 아이디어 :
아무것도 연결하지 않은채로 시작.
edge를 가장 작은것부터 연결한다.
k개의 components일때까지 연결한다. (자연스럽게 가장 큰것들은 0이 됨)

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
union-find

'''
class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        #union find
        # edges.sort(key=lambda x: x[2])
        # for i in range(k-1):
        #     edges.pop()
        # return edges[-1][2] if edges else 0

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return False
            
            if size[a] < size[b]:
                a, b = b, a
            
            par[b] = a
            size[a] += size[b]
            return True
        
        par = [i for i in range(n)]
        size = [1] * n

        edges.sort(key=lambda x: x[2])

        components = n
        ans = 0

        for u, v, w in edges:
            if components<=k:
                break
            
            if union(u, v):
                components -= 1
                ans = w
        
        return ans if components <= k else -1

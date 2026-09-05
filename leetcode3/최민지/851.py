class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj = [[] for _ in range(n)]
        
        # u -> v: u가 v보다 돈이 많음
        for u, v in richer:
            adj[v].append(u)
            
        res = [-1] * n
        
        def dfs(node):
            if res[node] != -1:
                return res[node]
            
            # 자기 자신이 일단 기본값
            min_quiet_person = node
            
            for parent in adj[node]:
                candidate = dfs(parent)
                if quiet[candidate] < quiet[min_quiet_person]:
                    min_quiet_person = candidate
                    
            res[node] = min_quiet_person
            return res[node]

        for i in range(n):
            dfs(i)
            
        return res
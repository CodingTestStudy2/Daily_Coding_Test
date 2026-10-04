'''
실패
'''
from collections import deque, defaultdict

class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(edges)
        lst = []
        for i in range(n-1):
            for j in range(i+1,n):
                tmp = edges.copy()
                del tmp[j]
                del tmp[i]
                dic = defaultdict(list)
                for a,b in tmp:
                    dic[a].append(b)
                    dic[b].append(a)
                visited = {}
                for k in range(n+1):
                    visited[k] = False
                results = []
                for k in range(n+1):
                    queue = deque()
                    if not visited[k]:
                        queue.append((k,nums[k]))
                        visited[k] = True
                    while queue:
                        elem,score = queue.pop()
                        # print(results)

                        if not elem in dic:
                            results.append(score)

                        if all([visited[x] for x in dic[elem]]):
                            results.append(score) 

                        for _next in dic[elem]:
                            if not visited[_next]:
                                queue.append((_next,score^nums[_next]))
                                visited[_next] = True
                            
                lst.append(max(results) - min(results))
        
        return min(lst)

from collections import defaultdict, deque

def solution(tickets):
    dic = defaultdict(list)
    for start,end in tickets:
        dic[start].append(end)
    dic2 = {}
    for key, value in dic.items():
        dic2[key] = sorted(value)

    visited = {}
    for key in dic2.keys():
        visited[key] = []

    n = sum([len(i) for i in dic2.values()])
    ans = None
    def dfs(lst):
        nonlocal ans
        if len(lst) == n + 1:
            ans = lst
            return
        
        last = lst[-1]
        if last in dic2:
            for key, value in dic2.items():
                if not value in visited[key]:
                    visited[key].append(value)
                    dfs(lst + [value])
        
        visited[key].remove(last)
        
        return 
    
    dfs(['ICN'])

        

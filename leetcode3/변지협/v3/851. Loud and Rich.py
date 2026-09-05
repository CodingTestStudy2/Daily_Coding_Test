"""
[[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]

0 (3) -> 1 (2) -> 2 (5)
       -> 3 (4) -> 4 (6)
            -> 5 (1)
            -> 6 (7)
1 > 0
2 > 1
3 > 1
3 > 7
4 > 3
5 > 3
6 > 3

bfs로 풀어보려고 했는데 시간초과가 난다.
"""

from collections import defaultdict, deque

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        dic = defaultdict(list)
        n = len(quiet)
        
        for x,y in richer:
            dic[y].append(x)

        ans = []

        for i in range(n):
            quiet_min = 99999
            quiet_person = -1
            queue = deque()
            queue.append(i)
            
            while True:
                if len(queue) == 0:
                    break
                
                element = queue.popleft()
                if quiet_min > quiet[element]:
                    quiet_min = quiet[element]
                    quiet_person = element
                
                if element in dic:
                    for j in dic[element]:
                        queue.append(j)
            
            ans.append(quiet_person)
        
        return ans
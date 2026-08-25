'''
그래프 그리다가 못풀었음.
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set_a, set_b = set(),set()

        n = len(graph)
        tmp = 0
        while True:
            # print('graph, tmp, set_a, set_b:', graph, tmp,set_a,set_b)
            if all([len(g) == 0 for g in graph]):
                break

            if len(graph[tmp]) == 0:
                if n-1 == tmp:
                    tmp = 0
                    continue
                else:
                    tmp += 1
                    continue

            element = graph[tmp].pop()
            graph[element].remove(tmp)
            
            if element in set_a and tmp in set_a:
                return False
            
            if element in set_b and tmp in set_b:
                return False
            
            if element in set_a:
                set_b.add(tmp)
                continue
            elif element in set_b:
                set_a.add(tmp)
                continue
            elif tmp in set_a:
                set_b.add(element)
                continue
            elif tmp in set_b:
                set_a.add(element)
                continue
        
            set_a.add(tmp)
            set_b.add(element)
            tmp = element

        print('graph, tmp, set_a, set_b:', graph, tmp,set_a,set_b)
        
        return True
                            

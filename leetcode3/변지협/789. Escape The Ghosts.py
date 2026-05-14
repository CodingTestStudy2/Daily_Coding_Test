'''
1. 아이디어 :
    ghost 거리가 target 거리보다 크면 탈출 가능 - 그냥 먼저 도달하면 됨
2. 시간복잡도 :
    O(n)
3. 자료구조/알고리즘 :
'''
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        me = abs(target[0]) + abs(target[1])
        g_lst = []
        for ghost in ghosts:
            g_lst.append(abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]))

        # print(g_lst)

        return True if me < min(g_lst) else False 
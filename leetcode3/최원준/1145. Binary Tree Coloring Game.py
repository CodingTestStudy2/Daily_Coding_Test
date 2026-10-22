#

'''
1. 아이디어 :
x 노드의 위치, x노드 위의 노드들의 합, x노드 왼쪽, 오른쪽 자식 노드들의 합을 비교합니다

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
bfs

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode | None, n: int, x: int) -> bool:


        def get_node_and_par_total(node: TreeNode):
            if node.val == x:
                return node, 0

            par_total = 0
            x_node = None

            queue = deque()
            queue.append(node)
            
            while queue:
                par = queue.popleft()
                if par == None: continue

                if par.val == x:
                    x_node = par
                else:
                    par_total += 1
                    queue.append(par.left)
                    queue.append(par.right)
            
            return x_node, par_total
        
        def get_child_value(node: TreeNode):
            total = 0
            if not node:
                return total
            
            queue = deque()
            queue.append(node)

            while queue:
                child = queue.popleft()
                if not child: continue

                total += 1
                queue.append(child.left)
                queue.append(child.right)
            return total

        x_node, par_total = get_node_and_par_total(root)
        left_total = get_child_value(x_node.left)
        right_total = get_child_value(x_node.right)

        return par_total > n - par_total or left_total > n - left_total or right_total > n - right_total
            


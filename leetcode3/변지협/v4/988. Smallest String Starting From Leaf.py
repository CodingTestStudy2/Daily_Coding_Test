'''
1. 아이디어 :
bfs로 모든 leaf 노드 탐색 후, 정렬하여 첫번째 요소를 정답으로 한다.

2. 시간복잡도 :
o(nlogn) (정렬)

3. 자료구조/알고리즘 :
bfs / 완전탐색
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        dic = {}
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        
        for i in range(len(alpha)):
            dic[str(i)] = alpha[i]

        queue = deque()
        
        queue.append((root, dic[str(root.val)]))
        snake = []
        
        while queue:
            node,curr= queue.pop()

            if node.left is None and node.right is None:
                snake.append(curr)

            if node.left:
                queue.append((node.left,dic[str(node.left.val)]+curr))
            if node.right:
                queue.append((node.right,dic[str(node.right.val)]+curr))
        
        snake.sort()
        
        return snake[0]
        
#

'''
1. 아이디어 :
- BST는 왼쪽_자식 < 부모 < 오른쪽_자식이어야 하고, inorder traversal을 하면 왼쪽, 부모, 오른쪽 순회를 합니다.
- 순회를 하면서 직전 값과 현재 값은 항상 prev < curr입니다.
- 만약 조건: prev >= curr 일 경우, prev 또는 curr이 문제.
- 1 2 3 4 5 를 순회할때,
    인접한 숫자들이 잘못되어있으면 (1 2 4 3 5) 조건이 1번 틀립니다. ( 4>3 )
    멀리 있는 숫자들이 잘못되어 있으면 (1 4 3 2 5) 조건이 2번 틀립니다. (4 > 3, 3 > 2)

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
inorder traversal

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def recoverTree(self, root: Optional[TreeNode]) -> None:
#         self.candids: list[TreeNode] = []
#         self.prev: TreeNode = None
#         """
#         Do not return anything, modify root in-place instead.
#         """
#
#         def dfs(node: TreeNode) -> None:
#             if not node:
#                 return
#
#             dfs(node.left)
#
#             if self.prev and self.prev.val > node.val: # 부모 값이 자식값보다 크다면,
#                 if not self.candids:
#                     self.candids.append(self.prev)
#
#                 if len(self.candids) == 1:
#                     self.candids.append(node)
#
#                 else:
#                     self.candids[1] = node
#
#             self.prev = node
#
#             dfs(node.right)
#
#         dfs(root)
#         self.candids[0].val, self.candids[1].val = self.candids[1].val, self.candids[0].val







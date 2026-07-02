# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#

'''
1. 아이디어 :
- key까지 찾아갑니다.
- 자식이 없을때: par 연결 끊기
- 자식이 1개 있을때: par을 자식과 연결
- 자식이 2개 있을때: par을 왼쪽 자식과 연결 + 오른쪽 자식을 왼쪽 자식의 가장 오른쪽에 연결

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
dfs

'''
class Solution:
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return None

        if node.val > key:
            node.left = self.deleteNode(node.left, key)
            return node
        if node.val < key:
            node.right = self.deleteNode(node.right, key)
            return node
        
        if not node.left:
            return node.right
        if not node.right:
            return node.left

        next_node = node.left
        while next_node.right:
            next_node = next_node.right
        
        next_node.right = node.right

        return node.left



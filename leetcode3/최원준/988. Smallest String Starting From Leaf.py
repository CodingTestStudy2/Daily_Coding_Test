# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#

'''
1. 아이디어 :
dfs를 통해 leaf까지 도달할때까지 char를 더합니다.
리턴조건은 4개:
- 리프 노드
- 왼쪽 노드만 존재
- 오른쪽 노드만 존재
- 중간 노드

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
dfs

'''
class Solution:
    def smallestFromLeaf(self, node: TreeNode | None, path: str = "") -> str:
        if not node:
            return ""
        
        path = chr(97 + node.val) + path

        if not node.left and not node.right:
            return path

        if not node.left:
            return self.smallestFromLeaf(node.right, path)
        
        if not node.right:
            return self.smallestFromLeaf(node.left, path)

        return min(
            self.smallestFromLeaf(node.left, path),
            self.smallestFromLeaf(node.right, path)
        )

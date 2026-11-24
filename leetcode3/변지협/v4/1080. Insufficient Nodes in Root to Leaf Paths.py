'''
1. 아이디어 :
dfs로 모든 leaf 노드 탐색 후, limit보다 작은 leaf 노드 제거 후, 부모 노드도 leaf 노드가 없으면 제거한다.

2. 시간복잡도 :
o(n) (dfs)

3. 자료구조/알고리즘 :
dfs
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode | None, limit: int) -> TreeNode | None:
        def dfs(node, presum):
            print(node.val, presum)
            if node.left is None and node.right is None:
                if presum < limit:
                    return None
                else:
                    return node

            if node.left is not None:
                node.left = dfs(node.left, presum + node.left.val)
            if node.right is not None:
                node.right = dfs(node.right, presum + node.right.val)

            print('here')

            if node.left is None and node.right is None:
                return None

            return node

        return dfs(root, root.val)
        
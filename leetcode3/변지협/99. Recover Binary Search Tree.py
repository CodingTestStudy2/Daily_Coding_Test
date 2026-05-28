# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
lst = []
diff = []
class Solution:
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        # print('inorder node:', node.val, node)
        lst.append(node.val)
        self.inorder(node.right)

    def inorder2(self, node):
        # print(node)
        if node is None:
            return
        if node.val in diff:
            node.val = diff[0] if not node.val == diff[0] else diff[1]
        self.inorder2(node.left)
        self.inorder2(node.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        # print(lst)
        lst_sorted = sorted(lst, key=lambda x:x)
        # print(lst_sorted)

        for i in range(len(lst_sorted)):
            if lst_sorted[i] != lst[i]:
                diff.append(lst_sorted[i])

        # print('diff:', diff)
        self.inorder2(root)
        lst.clear()
        diff.clear()
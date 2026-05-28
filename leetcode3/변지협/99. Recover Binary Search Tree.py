'''
1. 아이디어 :
    bst는 중위순회 시 오름차순이므로, 이걸 구하고 sorted 해서 다른 두개를 구함.
    다시 전체를 순회하면서 다른 두개를 바꿔준다.
2. 시간복잡도 :
    O(n)
3. 자료구조/알고리즘 :
    중위순회
'''


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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
serialize: input - tree, output - string
deserialize: input - string, output - tree

- BST: left child < parent < right child

serialize
- initialize the array
- iterate through the tree
    - dfs
    - append the value to the array
- return ','.join(array) 213

deserialize   213 -> tree


'''
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []

        def dfs(node):
            if not node:
                return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(arr)

        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
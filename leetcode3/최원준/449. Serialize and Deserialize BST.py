#

'''
1. 아이디어 :
pre_order로 순회하면서 str를 만듭니다.
pre_order는 가장 첫번째 숫자가 root, 그리고 왼쪽과 오른쪽을 나누는 경계선은 root의 숫자보다 커지기 시작하는 지점이므로,
binary search를 통해 계산합니다.

2. 시간복잡도 :
    O(n)
    O(nlogn)

3. 자료구조/알고리즘 :
pre_order traversal, binary search

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
     4
  2     6
1  3  5   7
"""

class Codec:

    def serialize(self, root: TreeNode | None) -> str:
        self.ans = ""

        def pre_order(node: TreeNode):
            if not node:
                return

            self.ans += str(node.val) + " "
            pre_order(node.left)
            pre_order(node.right)
        
        pre_order(root)
        return self.ans

        """Encodes a tree to a single string.
        """
        

    def deserialize(self, data: str) -> TreeNode | None:
        if not data:
            return None
        
        def build(lower, upper):
            if self.index == len(self.pre_order):
                return None
            
            val = self.pre_order[self.index]

            if val < lower or upper < val:
                return None
            
            self.index += 1
            par = TreeNode(val)
            par.left = build(lower, val)
            par.right = build(val, upper)

            return par

        self.pre_order = [int(d) for d in data.rstrip().split(" ")]
        self.index = 0
        return build(-float('inf'), float('inf'))
        """Decodes your encoded data to tree.
        """
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

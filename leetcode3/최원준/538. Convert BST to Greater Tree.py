#

'''
1. 아이디어 :
- 합을 구하기 위한 bfs
- 가장 작은 노드를 방문하기 위한 inorder

2. 시간복잡도 :
    O(n + n)

3. 자료구조/알고리즘 :
bfs, inorder traversal

'''
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0

        def get_total(node):
            return node.val + get_total(node.left) + get_total(node.right) if node else 0
        
        def recalculate(node):
            if not node:
                return
            
            recalculate(node.left)
            original = node.val
            self.total -= original
            node.val += self.total
            recalculate(node.right)
        
        self.total = get_total(root)
        recalculate(root)
        return root

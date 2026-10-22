# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        
        def get_num_list(node: TreeNode):
            num_list = []

            queue = deque()
            queue.append(node)
            
            while queue:
                curr = queue.popleft()
                if not curr:
                    continue
                
                num_list.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            return num_list
        
        queue = deque()
        queue.append(root)
        root_start_nodes = []

        while queue:
            curr = queue.popleft()
            if not curr: continue
            if curr.val == subRoot.val:
                root_start_nodes.append(curr)
            queue.append(curr.left)
            queue.append(curr.right)

        root_list = get_num_list(root_start_node)
        sub_root_lists = []
        for nodes in root_start_nodes:
            sub_root_lists.append(get_num_list(subRoot))
        
        ans = False
        for sub_root_list in sub_root_lists:
            if len(root_list) != len(sub_root_list):
                continue
            for i in range(len(root_list)):
                if root_list[i] != sub_root_list[i]:
                    break

        
        return ans


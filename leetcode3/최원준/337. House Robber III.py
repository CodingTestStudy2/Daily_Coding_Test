#

'''
1. 아이디어 :
bottom-up 방식으로 풀 수 있습니다.
dfs의 리턴값은 훔쳤을때의 최대값, 훔치지 않았을때의 최대값입니다.
- 현재 node를 훔치게 됐을때는, (현재node의 값 + 왼쪽에서 훔치지 않은 최대값 + 오른쪽에서 훔치지 않은 최대값),
- 현재 node를 훔치지 않을때는, max(왼쪽에서 훔쳤을때 최대값, 훔치지 않았을때 최대값) + max(오른쪽에서 훔쳤을때 최대값, 훔치지 않았을때 최대값)
마지막에 root에서는 둘 중 큰 값을 리턴합니다.

2. 시간복잡도 :
    O(n)

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
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(curr: TreeNode) -> list: # 훔쳤을때, 안훔쳤을떄
            if not curr:
                return [0, 0]
            curr_val = curr.val
            left_rob, left_clean = dfs(curr.left)
            right_rob, right_clean = dfs(curr.right)

            rob = left_clean + right_clean + curr_val
            clean = max(left_rob, left_clean) + max(right_rob, right_clean)

            return rob, clean

        rob, clean = dfs(root)
        return max(rob, clean)


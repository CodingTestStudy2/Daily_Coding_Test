
'''
1. 아이디어 :

2. 시간복잡도 :
    o(n^2)

3. 자료구조/알고리즘 :
bfs 형태로 문제를 풀었고, 각 노드의 값을 그 노드보다 크거나 같은 모든 노드의 값의 합으로 변경함
'''

from collections import deque
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # print(root)
        # print(root.left)
        # print(root.right)
        # print(root.left.left)
        # root.left.right.right.val = 12
        # print(root.left.right.right)

        if root is None:
            return None

        # 다 꺼낸다
        lst = []
        q = deque()
        q.append(root)
        
        while True:
            if len(q) == 0:
                break
            
            now = q.popleft()
            lst.append(now.val)
            # now.val = -1
            # print(now.val, root)
            
            if now.left is not None:
                q.append(now.left)
            if now.right is not None:
                q.append(now.right)

        q = deque()
        q.append(root)

        print(lst)
        
        while True:
            if len(q) == 0:
                break
            
            now = q.popleft()
            tmp_val = now.val
            # print('now.val, sum([i for i in lst if tmp_val > i]):', now.val, sum([i for i in lst if tmp_val <= i]))
            now.val = sum([i for i in lst if tmp_val <= i])
            
            if now.left is not None:
                q.append(now.left)
            if now.right is not None:
                q.append(now.right)

        # print(lst)
        return root

        # 탐색하면서 값 변경한다
        
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

'''
1. 아이디어 :
재귀로 풀 수 있습니다.
dfs에는 prev 노드와 curr 노드를 파라미터로 줍니다.
- curr 노드가 None이면, prev 노드를 리턴
- prev와 curr를 연결해줍니다.
- child를 계산한 후 연결할 next_node를 저장해둡니다.
- last는 child를 이어붙인 후, 마지막 노드를 의미합니다.
- dfs last와 next_node를 재귀적으로 호출.

dfs에 prev, curr이 필요하기떄문에 dummy노드를 만들어줍니다.
마지막에 dummy - head 연결을 끊어주고 head를 리턴합니다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :
dfs

'''

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dummy = Node(0, None, head, None)

        def dfs(prev, curr) -> Node:
            if not curr:
                return prev

            curr.prev = prev
            prev.next = curr

            next_node = curr.next

            last = dfs(curr, curr.child)
            curr.child = None

            return dfs(last, next_node)

        dfs(dummy, head)
        head.prev = None
        return head

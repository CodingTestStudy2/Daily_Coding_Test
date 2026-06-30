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
input: multi-level doublely linked list
output: single-level doubly linked list

- if not head, return None
- DFS 
    - curr
    - while curr
        - next_node = curr.next
        - if curr.child 
            - end_node = dfs(curr.child)      
            - curr.child.prev = curr
            - curr.next = curr.child
            - curr.child = None

            - if next_node
                - 

- iterate through the linked list
    - if child exist, move the pointer to the child
    - if node.next, move the pointer to next
- return head

TC: O(N), SC: O(N)
'''

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
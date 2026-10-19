# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        jump1 = head
        jump2 = head

        while jump2 and jump2.next:
            jump1 = jump1.next
            jump2 = jump2.next.next
            if jump1 == jump2:
                return True

        return False

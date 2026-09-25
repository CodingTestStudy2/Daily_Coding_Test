# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr=curr.next
        curr = head
        while curr:
            curr.val = nums.pop()
            curr = curr.next
        return head

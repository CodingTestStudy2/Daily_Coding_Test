#

'''
1. 아이디어 :
- 순차적으로 연결을 새롭게 만들며 계산 하는 방법
- 재귀적으로 끝에서부터 연결을 새롭게 만들며 계산 하는 방법

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head

'''
1. 아이디어 :
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
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        temp = []
        _next = head
        while True:
            val = _next.val
            _next = _next.next

            temp.append(val)

            if _next is None:
                break

        # temp = temp[::-1]
        prev = None
        for i in range(len(temp)):
            # if prev is not None:
                # print(prev.val)
            prev = ListNode(val=temp[i], next=prev)

        print(prev.next, prev.val)
        
        return prev
            
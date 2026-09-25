'''
1. 아이디어 :
DFS로 연결 리스트를 순회하면서 값을 리스트에 담는다.
리스트를 뒤집은 뒤, 끝에서부터 하나씩 꺼내 새 노드를 앞에 이어 붙여 뒤집힌 연결 리스트를 만든다.

2. 시간복잡도 :
o(n)

3. 자료구조/알고리즘 :
연결 리스트 / DFS(재귀), 리스트

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        lst = []
        def dfs(h: ListNode | None):
            if not h:
                return
            lst.append(h.val)
            dfs(h.next)
        
        dfs(head)
        tmp = None
        lst = lst[::-1]
        
        while lst:
            elem = lst.pop()
            if not tmp:
                tmp = ListNode(elem, None)
            else:
                tmp = ListNode(elem, tmp)
        
        return tmp

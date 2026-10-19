'''
실패했었는데, claude에게 방문처리 피드백 받고 다시 풀었다.
(처음엔 방문처리를 못해서 실패)

1. 아이디어 :
노드를 따라가면서 방문한 노드를 set에 저장한다.
다음 노드가 이미 set에 있으면 사이클이 있는 것이므로 True.
끝까지 가서 None을 만나면 사이클 없음(False).
방문처리(set)를 못해서 처음엔 못 풀었고, 피드백 받고 set으로 방문 기록하는 방식으로 다시 풀었다.

2. 시간복잡도 :
o(n)

3. 자료구조/알고리즘 :
연결 리스트 순회, set(해시) 방문 처리

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nxttmp = head
        visited = set()
        visited.add(nxttmp)
        while nxttmp:
            nxttmp = nxttmp.next

            if nxttmp in visited:
                return True
            visited.add(nxttmp)

        return False

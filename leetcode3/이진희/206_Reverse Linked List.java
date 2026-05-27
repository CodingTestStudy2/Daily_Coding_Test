/*

1. 아이디어 : 재귀와 링크드리스트 성질을 이용
            가장 마지막 노드까지 이동 후, 올라가면서 연결된 next를 끊고, 이전 노드를 앞 노드에 붙힌다

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 재귀

 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        return solve(head);
    }

    private ListNode solve(ListNode head) {
        if(head == null || head.next == null) return head;

        ListNode newListNode = solve(head.next);
        head.next.next = head;
        head.next = null;
        
        return newListNode;
    }
}
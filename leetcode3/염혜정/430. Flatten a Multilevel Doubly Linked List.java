// dfs 사용
// 시간복잡도 O(n)


class Solution {
    public Node flatten(Node head) {
        // DFS
        dfs(head);
        return head;
    }

    Node dfs(Node node) {
        Node curr = node;
        Node last = null;

        while (curr != null) {
            Node next = curr.next;

            if (curr.child != null) {
                Node childTail = dfs(curr.child);

                curr.next = curr.child;
                curr.child.prev = curr;
                curr.child = null;

                if (next != null) {
                    childTail.next = next;
                    next.prev = childTail;
                }
                last = childTail;
            } else {
                last = curr;
            }
            curr = next;
        }
        return last;
    }
}

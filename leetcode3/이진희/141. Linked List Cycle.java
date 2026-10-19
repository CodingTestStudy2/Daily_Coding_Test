/*

1. 아이디어 : 모든 노드 탐색, 탐색한 노드는 입력 범위를 벗어나는 숫자로 변경
             입력범위 벗어나는 숫자 존재시 cycle

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 링크드리스트 구조

 */


public class Solution {

    boolean check;
    public boolean hasCycle(ListNode head) {

        check = false;
        findCycle(head); 

        return check;
    }

    private void findCycle(ListNode node) {
        if(node == null) return;

        if(node.val == 100001) {
            check = true;
            return;
        }
        node.val = 100001;

        findCycle(node.next);
    }
}
/* 

1. 아이디어 :
          - 오른쪽 -> 왼쪽으로 탐색하며 단조 감소 스택 유지
          - 탐색중 idx 키가 자료구조 peek값보다 크다면, idx보다 키가 작은 원소는 모두 pop하며 카운트
          - 전부 pop 이후 원소가 남으면 1명 추가
          - pop한 원소는 현재 사람에게 가려지므로 stack 자료구조에서 제거

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 스택 자료구조 (Deque)

 */

class Solution {
    public int[] canSeePersonsCount(int[] heights) {
        Deque<Integer> dq = new ArrayDeque<>();

        int[] ans = new int[heights.length];

        for(int i=heights.length-1; i>=0; i--) {
            int h = heights[i];
            int cnt = 0;

            while(!dq.isEmpty() && dq.peek() < h) {
                dq.pop();
                cnt++;
            }

            if(!dq.isEmpty()) cnt++;
            ans[i] = cnt;

            dq.push(h);
        }

        return ans;
    }
}
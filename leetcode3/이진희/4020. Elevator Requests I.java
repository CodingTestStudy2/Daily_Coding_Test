/*

1. 아이디어 : 각 배열 숫자의 차이의 절댓값 더하기 Math.abs(requests[i]-requests[i-1]) + requests[0] (첫번째 층까지 올라가는 층수)

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int elevatorRequests(int n, int[] requests) {
        int ans = 0;
        for(int i=1; i<requests.length; i++) ans+=Math.abs(requests[i]-requests[i-1]);

        return ans+requests[0];
    }
}
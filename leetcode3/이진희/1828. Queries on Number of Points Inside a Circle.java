/*

1. 아이디어 : 수학

2. 시간복잡도 : O(N*M) (각 배열 크기의 곱)

3. 자료구조/알고리즘 : 완전탐색, 원 방정식 (a^2 + b^2 = r^2)

 */

class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        // 원 내부의 점 개수 구하기
        // 특정 점과 중심 사이의 거리

        int[] ans = new int[queries.length];
        int idx = 0;

        for(int[] query : queries) {
            int y = query[0];
            int x = query[1];
            int r = query[2];

            int cnt = 0;
            for(int[] point : points) {
                int calY = point[0]-y;
                int calX = point[1]-x;

                int dist = calY*calY + calX*calX;
                if(dist <= r*r) cnt++;
            }

            ans[idx++] = cnt;
        }

        return ans;
    }
}
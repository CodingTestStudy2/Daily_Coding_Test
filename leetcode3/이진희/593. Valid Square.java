/*
1. 아이디어: 4점이 주어졌을때 정사각형 판별 - 정사각형의 성질 활용
           1. 4변의 길이가 같다 
           2. 두 대각선의 길이가 같다

2. 시간복잡도: O(1);

3. 자료구조/알고리즘: 정렬, 정사각형 성질(수학)

*/

class Solution {
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {

        int[] dis = new int[6];
        dis[0] = dist(p1, p2);
        dis[1] = dist(p1, p3);
        dis[2] = dist(p1, p4);
        dis[3] = dist(p2, p3);
        dis[4] = dist(p2, p4);
        dis[5] = dist(p3, p4);
        

        // 마지막 2개 원소가 대각선
        Arrays.sort(dis);

        if(dis[0] == 0) return false;
        
        return dis[0] == dis[1] &&
               dis[1] == dis[2] &&
               dis[2] == dis[3] &&
               dis[4] == dis[5];
    }
    
    private int dist(int[] a, int[] b) {
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]);
    }
}
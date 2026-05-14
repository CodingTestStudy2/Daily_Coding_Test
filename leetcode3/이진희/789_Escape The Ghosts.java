/*

1. 아이디어 : 유령이 먼저 target 위치에 도착시 무조건 잡힘
            현 유령 위치와 도착지 사이의 거리를 계산하여, 하나라도, 플레이어보다 빠르게 도착하면 짐

2. 시간복잡도 : O(100)

3. 자료구조/알고리즘 : 그리디

 */

class Solution {
    public boolean escapeGhosts(int[][] ghosts, int[] target) {
        
        int dis = Math.abs(target[0]) + Math.abs(target[1]);

        for(int[] ghost : ghosts) {
            int y = ghost[0];
            int x = ghost[1];

            int ghostDis = Math.abs(target[0] - y) + Math.abs(target[1] - x);
            if(dis >= ghostDis) return false;
        }    

        return true;
    }
}
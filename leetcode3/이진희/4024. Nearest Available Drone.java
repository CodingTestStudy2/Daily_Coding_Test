/*

1. 아이디어 : 가장 가까운 범위를 만족하는 드론 찾기

2. 시간복잡도 : O(100)

3. 자료구조/알고리즘 : 계산

 */

class Solution {
    public int nearestDrone(int[][] drones, int[] target) {
        // 더 가까운 드론 찾기

        int idx = -1;
        int minDis = 10000000;

        for(int i=0; i<drones.length; i++) {
            int len = Math.abs(drones[i][0] - target[0]) + Math.abs(drones[i][1] - target[1]);
            if(drones[i][2]<len || minDis<=len) continue;
            
            minDis = len;
            idx = i;
        }

        return idx;
    }
}
/* 

1. 아이디어 : 기하학의 원리 활용
            직사각형은 x,y축과 평행하므로 원과 가장 가까운 점을 찾는다.
            그 점과 원의 중심사이의 거리가 반지름보다 크다면 겹치지않고, 이하라면 겹침

2. 시간복잡도 : O(1)

3. 자료구조/알고리즘 : 기하학

 */

class Solution {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        // 겹치면 true, 아니면 false
        
        int y = Math.max(y1, Math.min(y2, yCenter));
        int x = Math.max(x1, Math.min(x2, xCenter));

        if(((y-yCenter)*(y-yCenter) + (x-xCenter)*(x-xCenter))<=radius*radius) return true;

        return false;
    }
}
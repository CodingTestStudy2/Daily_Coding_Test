/*

1. 아이디어 : 두 사각형의 겹치는 영역 구하기
            좌하단에서 우상단 순서의 좌표이므로, 좌하단은 가장 큰값
            우 상단은 가장 작은 값을 구해야 겹치는 영역을 구할 수 있다

            두 사각형이 안겹칠수도 있기 때문에, 겹치는 사각형의 높이와 너비중 0이하인 수가 있는지 확인해야한다

2. 시간복잡도 : O(1)

3. 자료구조/알고리즘 : 수학

 */

class Solution {
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        // 전체 영역 구하기
        // 24 + 27 - 6 = 45

        int totalSum = (ay2-ay1)*(ax2-ax1) + (by2-by1)*(bx2-bx1);

        int cx1 = Math.max(ax1, bx1);
        int cy1 = Math.max(ay1, by1);

        int cx2 = Math.min(ax2, bx2);
        int cy2 = Math.min(ay2, by2);

        int width = cx2 - cx1;
        int height = cy2 - cy1;
        
        if(width > 0 && height > 0) totalSum -= width*height;

        return totalSum;
    }
}
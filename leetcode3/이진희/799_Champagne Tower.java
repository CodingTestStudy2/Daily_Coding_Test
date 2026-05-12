/*

1. 아이디어 : 물을 담을 공간을 미리 선언 -> 최대 101*101
            각 잔은 최대 1의 물을 담을 수 있고, 넘친다면 1/2씩 아랫잔으로 분배됨
            맨처음 잔에 모든 물을 담고(poured), row 만큼 내려가며 넘치는 물을 분배해줌
            1차원 배열로 DP를 선언 했다면 더 빨랐을것 같음..

2. 시간복잡도 : O(query_row^2)

3. 자료구조/알고리즘 : DP

 */

class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] tower = new double[101][101];

        tower[0][0] = (double)poured;

        for(int i=0; i<query_row+1; i++) {
            for(int j=0; j<=i; j++) {
                double extra = (tower[i][j] - 1.0) / 2.0;

                if(extra > 0) {
                    tower[i+1][j] += extra;
                    tower[i+1][j+1] += extra;
                }
            }
        }

        double ans = Math.min(1, tower[query_row][query_glass]);
        return ans;
    }
}
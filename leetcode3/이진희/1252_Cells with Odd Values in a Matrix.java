/*

1. 아이디어 : 행렬을 직접 만들면 비효율적이므로, 행과 열의 증가 횟수만 독립적으로 카운트
              특정 위치의 값이 홀수가 되려면 (행 홀수 + 열 짝수) 또는 (행 짝수 + 열 홀수)
              즉 홀수 증가된 행열의 개수를 구해 최종 계산

2. 시간복잡도 : O(L + m + n) (L = indices)

3. 자료구조/알고리즘 : 수학

 */

class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int[] rows = new int[m];
        int[] cols = new int[n];
        
        for (int[] index : indices) {
            rows[index[0]]++;
            cols[index[1]]++;
        }
        
        int oddRows = 0;
        for (int r : rows) {
            if (r % 2 != 0) {
                oddRows++;
            }
        }
        
        int oddCols = 0;
        for (int c : cols) {
            if (c % 2 != 0) {
                oddCols++;
            }
        }
        
        int evenRows = m - oddRows;
        int evenCols = n - oddCols;
        
        return (oddRows * evenCols) + (evenRows * oddCols);
    }
}
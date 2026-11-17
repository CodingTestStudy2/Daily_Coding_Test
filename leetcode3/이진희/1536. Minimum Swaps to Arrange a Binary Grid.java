/*
1. 아이디어:
   - row를 swap하여 대각선 위 모든 원소를 0으로 바꿀 수 있는지 확인, 있다면 최소 swap 비용 return 
   - 완전탐색을 사용한다
   - 미리 각 row의 오른쪽부터 연속된 0의 개수를 파악한 후 완전탐색으로 swap하며 계산

2. 시간복잡도: O(N^2)

3. 자료구조/알고리즘: 완전탐색
*/

class Solution {
    public int minSwaps(int[][] grid) {
        int ans = 0;
        int n = grid.length;

        int[] cnt = new int[n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++) {
                if(grid[i][n-j-1] != 0) break;
                cnt[i]++;
            }
        }

        boolean[] used = new boolean[n];

        for(int i=0; i<n; i++) {
            int dist = 0;
            int check = -1;
            for(int j=0; j<n; j++) {
                if(used[j]) continue;
                if(cnt[j] >= n-1-i) {
                    check = j;
                    break;
                }
                dist++;
            }
            if(check == -1) return -1;
            used[check] = true;
            ans+=dist;
        }

        return ans;
    }
}
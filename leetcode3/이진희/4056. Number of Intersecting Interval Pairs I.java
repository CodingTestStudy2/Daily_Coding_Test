/*

1. 아이디어 : 각 구간의 시작점과 끝점이 주어졌을때, 구간별 겹치는 개수 파악하기
            두 구간이 겹치는 경우의 수는 포함과 일부 겹침 두개가 존재하므로, 겹치지 않는 경우로 체크
            모든 배열을 완전탐색해서 구간 a의 end가 구간 b의 start보다 작거나 반대 경우만 제외

2. 시간복잡도 : O(N^2)

3. 자료구조/알고리즘 : 완전탐색 

 */

class Solution {
    public int countIntersectingIntervals(int[][] intervals) {

        int len = intervals.length;
        int ans = 0;

        for(int i=0; i<len-1; i++) {
            for(int j=i+1; j<len; j++) {
                if(intervals[i][1] < intervals[j][0] || intervals[j][1] < intervals[i][0]) continue;
                ans++;
            }
        }

        return ans;
    }
}
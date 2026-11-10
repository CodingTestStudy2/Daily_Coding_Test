/*
1. 아이디어:
   - 최적화 문제를 결정 문제로 변환할 수 있어야 한다
   - 최대 force로 작용하는 곳에 공을 두고, 두 공 사이의 최소 자기장의 force를 구해야함
   - 이때, k에 따라 모든 공 m을 position 배열 안에 배치된 바스켓에 전부 넣을수 있는지 없는지 판단해야한다

2. 시간복잡도: O(log(position[position.length-1] - position[0])*N)

3. 자료구조/알고리즘: 이분탐색 (파라메트릭 서치)
*/

class Solution {
    public int maxDistance(int[] position, int m) {
        // 최대로 자기력이 작용하는 거리에 공을 둠
        // 이때 가장 가까운 basket의 거리

        Arrays.sort(position);
        // force가 k일때 m개의 공 배치

        int left = 1;
        int right = position[position.length-1] - position[0];

        int ans = 0;
        while(left<=right) {
            int mid = left+(right-left)/2;
            if(canPlace(position, m, mid)) {
                ans = mid;
                left = mid+1;
            }
            else right = mid-1;
        }    

        return ans;    
    }

    private boolean canPlace(int[] position, int m, int k) {
        int cnt = 1;
        int last = position[0];  

        for(int i=1; i<position.length; i++) {
            int curr = position[i];
            int dist = curr - last;

            if(dist >= k) {
                cnt++;
                last = curr;
            }

            if(cnt==m) return true;
        }
        
        return false;
    }
}
/* 

1. 아이디어 : HashMap 자료구조의 특징 활용
            한 점을 기준점으로 잡고, 두점 사이의 거리가 같은 개수를 셈 
            이후 모든 경우의 수를 계산

2. 시간복잡도 : O(N^2)

3. 자료구조/알고리즘 : HashMap 자료구조 특징, 두 점사이의 거리

 */

class Solution {
    public int numberOfBoomerangs(int[][] points) {
        // i and j 거리 == i and k 거리
        // 최대 500개의 고유한 튜플
        // 22 33 11  22 11 33 (절댓값)

        int ans = 0;
        Map<Integer, Integer> map = new HashMap<>(); // 매번 객체 생성 불필요

        // (jy - iy)^2 + (jx - ix)^2 = (ky - iy)^2 + (kx - ix)^2
        
        for(int i=0; i<points.length; i++) {
            for(int j=0; j<points.length; j++) {
                
                if(i==j) continue;

                int diffY = points[i][1] - points[j][1];
                int diffX = points[i][0] - points[j][0];

                int distance = diffY*diffY + diffX*diffX;

                if(!map.containsKey(distance)) map.put(distance, 1);
                else map.put(distance, map.get(distance)+1);
            }

            for(int key : map.keySet()) {
                int value = map.get(key);
                ans += value*(value-1);
            }

            map.clear();
        }

        return ans;
    }
}
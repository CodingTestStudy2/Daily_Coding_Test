/*

1. 아이디어 : 완전탐색으로 물건을 담을 수 있는 최소 사이즈 박스를 찾는다
            이때 박스 사이즈가 같을경우 가장 작은 인덱스를 반환하므로 현재 for문에서 박스 사이즈가 같을 경우는 고려하지 않는다

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int minimumIndex(int[] capacity, int itemSize) {
        // 가장 작은 용량의 박스
        // 여러개일 경우 가장 작은 인덱스 

        int minIdx = 200;
        int minSize = 200;

        for(int i=0; i<capacity.length; i++) {
            int size = capacity[i];

            if(itemSize>size) continue;
            if(minSize>size) {
                minSize = size;
                minIdx = i;
            }
        }
        
        if(minIdx == 200) return -1;
        return minIdx;
    }
}
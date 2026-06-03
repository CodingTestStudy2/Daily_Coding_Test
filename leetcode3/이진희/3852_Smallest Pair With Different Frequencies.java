/*

1. 아이디어 : 조건을 만족하는 가장 작은 x,y쌍 구하기 (이때 x가 같은 쌍이 여러개면 y가 제일 작은 값으로)
            
            조건
            1. x<y 
            2. x와 y의 빈도수는 달라야한다

            각 수의 빈도수를 저장할 배열 선언후 미리 계산
            이중 for문으로 완전 탐색을 진행해서 구한다
            이때, 값이 구해지면 바로 return하여 가지치기 가능

2. 시간복잡도 : O(N^2)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int[] minDistinctFreqPair(int[] nums) {
        // 조건
        // x < y
        // x와 y의 빈도수 달라야함

        // 답
        // 가장 작은 x
        // x가 많다면 가장 작은 y

        int[] cnt = new int[101];

        for(int i : nums) {
            cnt[i]++;
        }

        return findNums(cnt);
    }

    private int[] findNums(int[] cnt) {
        for(int i=1; i<100; i++) {
            if(cnt[i] == 0) continue;
            for(int j=i+1; j<101; j++) {
                if(cnt[j] == 0) continue;
                if(cnt[i] == cnt[j]) continue;

                return new int[] {i, j};
            }
        }
        return new int[] {-1,-1};
    }
}
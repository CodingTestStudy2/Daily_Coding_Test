/*

1. 아이디어 : 총 배열의 크기는 2만이지만, 나이는 120살까지 제한됨
            121크기의 배열을 만들어, 각 나이대별 인원을 구하고, 완전탐색으로 계산
            이때 서로 나이가 같을 경우 -> age[i] * (age[i]-1)
            서로 다를 경우 -> age[i] * age[j]

2. 시간복잡도 : O(N^2) -> O(14400)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int numFriendRequests(int[] ages) {
        int[] age = new int[121];
        for (int a : ages) age[a]++;
        
        int ans = 0;

        for (int i = 1; i < 121; i++) {
            if (age[i] == 0) continue;
            for (int j = 1; j < 121; j++) {
                if (age[j] == 0) continue;     
                if (!isPossible(i, j)) continue;
                if (i == j) ans += age[i] * (age[i] - 1);
                else ans += age[i] * age[j];
            }
        }
        return ans;
    }

    static boolean isPossible(int x, int y) {
        if (y <= 0.5 * x + 7) return false;
        if (y > x) return false;
        if (y > 100 && x < 100) return false;
        return true;
    }
}
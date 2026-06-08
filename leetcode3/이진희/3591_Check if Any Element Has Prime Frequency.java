/*

1. 아이디어 : 에라토스테네스의 체와 빈도수 배열 사용
              100 까지 의 수므로 미리 각 숫자의 등장 빈도수와 100 이하의 소수를 구한다
              이후 빈도수 배열을 완전탐색해 소수가 존재하는지 찾는다

2. 시간복잡도 : O(N) + O(M log log M) + O(N) => O(N) (M=100)

3. 자료구조/알고리즘 : 에라토스테네스의 체, 빈도수 배열

 */

class Solution {
    public boolean checkPrimeFrequency(int[] nums) {
        // 특정 수의 등장 횟수가 소수면 return true

        int[] cnt = new int[101];
        for(int i : nums) {
            cnt[i]++;
        }

        boolean[] isNotPrime = new boolean[101];
        isNotPrime[0] = isNotPrime[1] = true;

        for(int i=2; i*i<101; i++) {
            for(int j=i*i; j<101; j+=i) {
                isNotPrime[j] = true;
            }
        }

        for(int i : cnt) {
            if(isNotPrime[i]) continue;
            return true;
        }
        return false;
    }
}
// prefix의 길이가 짝수면 0과 1의 개수가 같아야 하고
// prefix의 길이가 홀수면 0과 1의 개수의 차이가 1이어야 함
// O(n)

class Solution {
    public int countValidPrefixes(String s) {
        int[] cnt = new int[2];
        int result = 0;

        for (int i = 0; i<s.length(); i++) {
            cnt[s.charAt(i) - '0']++;
            
            if ((i+1) % 2 == 0) {
                if (cnt[0] == cnt[1]) result++;
            } else {
                if (Math.abs(cnt[0] - cnt[1]) == 1) result++;
            }
        }
        return result;
    }
}

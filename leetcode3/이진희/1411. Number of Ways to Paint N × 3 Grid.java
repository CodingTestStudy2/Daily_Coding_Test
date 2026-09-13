/* 2차 풀이

1. 아이디어 : DP로 풀이 3가지 색깔을 겹치치않게 사용할 경우 패턴은 ABA와 ABC 존재
            각 ABA -> ABC, ABA -> ABA, ABC -> ABC, ABC -> ABA 경우의 수를 각각 구해 dp로 계산
            이때 2차원 DP를 따로 선언하지 않음(직전 상태값만 필요하므로) - 3ms

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : DP

 */

class Solution {
    public int numOfWays(int n) {
        // 인접한 칸이 같은 색이면 안됨
        // 10^9 + 7의 나머지

        int MOD = 1_000_000_000 + 7;

        // ABA = 6
        // ABC = 6

        // ABA -> BAB, CAC, BCB (3)
        // ABA -> BAC, CAB (2)
        // ABC -> BCA, CAB (2)
        // ABC -> BAB, BCB (2)

        long aba = 6;;
        long abc = 6;
        
        for(int i=1; i<n; i++) {
            long nextABA = (aba*3 + abc*2)%MOD;
            long nextABC = (abc*2 + aba*2)%MOD;

            aba = nextABA;
            abc = nextABC;
        }


        return (int)(aba+abc)%MOD;
    }   
}

/* 1차 풀이

1. 아이디어 : DP로 풀이 3가지 색깔을 겹치치않게 사용할 경우 패턴은 ABA와 ABC 존재
            각 ABA -> ABC, ABA -> ABA, ABC -> ABC, ABC -> ABA 경우의 수를 각각 구해 dp로 계산
            6ms 소요

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : DP

 */

class Solution {
    public int numOfWays(int n) {
        // 인접한 칸이 같은 색이면 안됨
        // 10^9 + 7의 나머지

        int MOD = 1_000_000_000 + 7;

        // ABA = 6
        // ABC = 6

        // ABA -> BAB, CAC, BCB (3)
        // ABA -> BAC, CAB (2)
        // ABC -> BCA, CAB (2)
        // ABC -> BAB, BCB (2)

        long[][] dp = new long[2][n];
        // ABA
        dp[0][0] = 6;
        // ABC
        dp[1][0] = 6;
        
        for(int i=1; i<n; i++) {
            dp[0][i] = (dp[0][i-1]*3 + dp[1][i-1]*2)%MOD;
            dp[1][i] = (dp[1][i-1]*2 + dp[0][i-1]*2)%MOD;
        }


        return (int)(dp[0][n-1] + dp[1][n-1])%MOD;
    }   
}
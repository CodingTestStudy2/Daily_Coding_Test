/*
1. 아이디어: 크기가 1보다 큰 파티션으로 배열 나누기
             이때 각 파티션은 같은 숫자로만 이루어져야 한다.
             
             최대공약수 - 유클리드 호제법 사용. 
             먼저 숫자의 빈도수를 세고, 첫 빈도수 기준 최대 공약수를 각각 계산한다.

2. 시간복잡도: O(10000*logN)

3. 자료구조/알고리즘: 최대공약수, 카운팅

*/

class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        int[] cnt = new int[10001];

        for(int i=0; i<deck.length; i++) cnt[deck[i]]++;

        int g = -1;
        for(int i=0; i<10001; i++) {
            if(cnt[i] == 0) continue;
            
            if(g == -1) g = cnt[i]; 
            else g = gcd(g, cnt[i]);
        }
        return g > 1;

    }

    private int gcd(int a, int b) {
        if(b==0) return a;
        return gcd(b, a%b);
    }
}
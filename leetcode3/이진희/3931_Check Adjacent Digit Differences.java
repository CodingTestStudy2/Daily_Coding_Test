/*

1. 아이디어 : 인접한 두 수의 거리가 3 이상이면 false, 반복문을 통해 구한다

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public boolean isAdjacentDiffAtMostTwo(String s) {
        int[] num = new int[s.length()];

        for(int i=0; i<s.length(); i++) num[i] = s.charAt(i)-'0';
        for(int i=0; i<num.length-1; i++) {
            if(Math.abs(num[i] - num[i+1])>2) return false;
        }
        return true;
    }
} 
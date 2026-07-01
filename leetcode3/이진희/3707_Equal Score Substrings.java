/*

1. 아이디어 : 미리 모든 알파벳의 합을 구한다. 이후, 슬라이딩 윈도우 기법으로 직접 잘라보며 값이 같아지는지 판단한다.

2. 시간복잡도 : O(2*N)

3. 자료구조/알고리즘 : 슬라이딩 윈도우

 */

class Solution {
    public boolean scoreBalance(String s) {
        // 잘라서 합이 같아야함
        // 1부터 n-1까지 자르기 가능

        int leftSum = 0;
        int rightSum = 0;
        for(int i=0; i<s.length(); i++) {
            leftSum+=s.charAt(i)-'a'+1;
        }

        for(int i=0; i<s.length(); i++) {
            leftSum-=s.charAt(i)-'a'+1;
            rightSum+=s.charAt(i)-'a'+1;

            if(leftSum == rightSum) return true;
        }

        return false;
    }
}
/*

1. 아이디어 : 다이얼 크기 10 -> 시계방향, 반시계방향 회전의 경우중 더 짧은것 선택
             
             경우의 수 (a->b)
             1. |a-b|
             2. 9 - |a-b|

2. 시간복잡도 : O(s 문자열 길이)

3. 자료구조/알고리즘 : 그리디

 */

class Solution {
    public int minRotations(String s) {
        
        int ans = 0;
        int pos = 0;

        for(int i=0; i<s.length(); i++) {
            int num = s.charAt(i)-'0';

            // 회전해서 갈 경우
            // 바로 갈 경우

            int cal = Math.abs(num-pos);

            ans+=Math.min(cal, 10-cal);

            pos = num;
        }

        return ans;
    }
}
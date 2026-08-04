/*

1. 아이디어 : 최대 n자리 만큼의 합이 s인 가장 큰 수 이므로, 생각해봤을때 9를 맨 앞에 배치하는게 제일 크다

2. 시간복잡도 : O(n/9 + n%9) - n은 최대 5이므로 길이가 5초과일때 return 하면 시간 복잡도를 줄일 수 있을것 같다

3. 자료구조/알고리즘 : 그리디

 */

class Solution {
    public int largestInteger(int n, int s) {
     // 최대 n자리의 가장 큰 수 (합이 s인)
     // 구할 수 없다면 -1

     if(s == 0) return 0;

     int x = s/9;
     int remain = s%9;

     StringBuilder sb = new StringBuilder();
     
     for(int i=0; i<x; i++) sb.append(9);
     if(remain>0) sb.append(remain);

     while(sb.length()<n) sb.append(0);

     int ans = 0;
     for(int i=0; i<sb.length(); i++) ans = ans*10+sb.charAt(i)-'0';

     if(sb.length()>n) return -1;
     return ans;
    }
}
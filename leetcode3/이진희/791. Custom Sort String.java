/* 

1. 아이디어 : 두개의 StringBuilder 사용 (sorted, left)
              s 문자열 부터 순회하며 각 문자열 개수를 카운팅 
              order 문자열을 순회하며, s 문자열에 order 문자열이 존재할 경우 카운팅 개수만큼 붙임 (sorted)
              다시 s 문자열을 순회하며 카운팅 배열에 개수가 남아있는 경우 붙임 (left)

              완료 후 sorted + left 문자열을 합쳐서 반환

2. 시간복잡도 : O(order 문자열 길이 + 2*s 문자열 길이) = O(N)

3. 자료구조/알고리즘 : 카운팅 배열 + 완전탐색

 */

class Solution {
    public String customSortString(String order, String s) {
        // 매칭된 문자열 순서 유지
        // 나머지 문자 배열

        int[] cnt = new int[26];
        StringBuilder sorted = new StringBuilder();
        StringBuilder left = new StringBuilder();

        for(int i=0; i<s.length(); i++) {
            cnt[s.charAt(i)-'a']++;
        }

        for(int i=0; i<order.length(); i++) {
            char c = order.charAt(i);

            if(cnt[c-'a']>0) {
                while(cnt[c-'a']>0) {
                    sorted.append(c);
                    cnt[c-'a']--;
                }
            }

        }

        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(cnt[c-'a'] <= 0) continue;
            left.append(c);
        }

        return sorted.toString() + left.toString();
    }
}
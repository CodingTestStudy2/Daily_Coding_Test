/* 

1. 아이디어 : 1순위 빈도수가 같은 알파벳 모음중 가장 큰 것
              2순위 빈도수가 가장 많은 것
              
              // 먼저 알파벳 빈도수대로 기록 후 조건에 맞게 계산

2. 시간복잡도 : O(N) + O(N) + O(26) + O(N) => O(N)

3. 자료구조/알고리즘 : 구현

 */

class Solution {
    public String majorityFrequencyGroup(String s) {
        int[] cnt = new int[26];
        List<List<Character>> list = new ArrayList<>();

        for(int i=0; i<s.length(); i++) {
            cnt[s.charAt(i)-'a']++;
        }

        for(int i=0; i<101; i++) list.add(new ArrayList<>());

        for(int i=0; i<26; i++) {
            if(cnt[i]==0) continue;
            list.get(cnt[i]).add((char)(i+'a'));
        }

       int maxGroupSize = 0;
       int maxFrequency = 0;

       List<Character> ans = new ArrayList<>();

       for(int i=0; i<101; i++) {
        List<Character> curr = list.get(i);

        int currSize = curr.size();

        if(maxGroupSize<currSize || ((maxGroupSize==currSize) && currSize > 0)) {
            maxGroupSize = currSize;
            maxFrequency = i;
            ans = curr;
        }

       }

       StringBuilder sb = new StringBuilder();
       for(char c : ans) {
          sb.append(c);
       }

       return sb.toString();
    }
}
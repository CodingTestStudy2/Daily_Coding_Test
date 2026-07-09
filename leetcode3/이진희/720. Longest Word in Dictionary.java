/*

1. 아이디어 : 모든 부분 배열(a, ab, abc..)을 가진 가장 긴 문자열을 찾는다. 중복이라면 사전순으로 가장 빠른 것을 답으로 한다.
              정렬을 먼저 진행. 길이가 2 이상부터는 배열에 각 문자열의 len-1글자가 존재하지 않으면 답이 될 수 없다.
              정렬 후, Set을 이용하여, 답이 될 수 있는 후보들을 체크하며 갱신한다. 
              이때, 한글자도 답이 될 수 있으므로, 사전순으로 가장 빠른 글자를 확인해야 한다.

2. 시간복잡도 : O(NlogN) + O(N)*O(L) => O(NlogN) (N: words 배열의 크기, L: 문자열의 최대 길이)

3. 자료구조/알고리즘 : Set, 정렬

 */

class Solution {
    public String longestWord(String[] words) {
        // 단어의 모든 부분 배열이 존재(왼쪽부터)
        // 여러개일 경우 1.가장 긴 길이, 2.사전순으로 제일 첫번째

        // a, ap, app, app1, apply, apple, banana

        Set<String> set = new HashSet<>();
        Arrays.sort(words);
        String ans = "";
        boolean hasOne = false;

        for(String s : words) {
            if(s.length() == 1) {
                set.add(s);
                if(!hasOne) ans = s;
                hasOne = true;
            }
            else {
                if(!set.contains(s.substring(0, s.length()-1))) continue;
                set.add(s);

                if(ans.length()>=s.length()) continue;
                ans = s;
            }
        }

        return ans; 
    }
}
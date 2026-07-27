/*

1. 아이디어 : 조건에 맞춰 구현
              리스트를 사용하여 각 문자열을 압축, 각각의 개수 구함
              words 배열을 완전탐색하여 똑같이 계산 후, 늘릴수 있는지, 조건에 맞춰 하나하나 비교

2. 시간복잡도 : O(S+N*M) (N = words.length, M = words 배열의 각 단어의 길이)

3. 자료구조/알고리즘 : 구현

 */

class Solution {
    private List<int[]> ori;

    public int expressiveWords(String s, String[] words) {
        ori = new ArrayList<>();
        char memo = s.charAt(0);
        int cnt = 1;
        int ans = 0;

        for(int i=1; i<s.length(); i++) {
            char c = s.charAt(i);
            if(c != memo) {
                ori.add(new int[]{memo, cnt});
                memo = c;
                cnt = 1;
            }
            else cnt++;
        }
        ori.add(new int[]{memo, cnt});

        for(String word : words) {
            if(checkExpressiveWords(word)) ans++;
        }

        return ans;
    }

    private boolean checkExpressiveWords(String s) {
        List<int[]> tmp = new ArrayList<>();
        char memo = s.charAt(0);
        int cnt = 1;
        int ans = 0;

        for(int i=1; i<s.length(); i++) {
            char c = s.charAt(i);
            if(c != memo) {
                tmp.add(new int[]{memo, cnt});
                memo = c;
                cnt = 1;
            }
            else cnt++;
        }
        tmp.add(new int[]{memo, cnt});

        if(tmp.size() != ori.size()) return false;
        for(int i=0; i<tmp.size(); i++) {
            int[] o = ori.get(i);
            int[] t = tmp.get(i);

            if(o[0] != t[0]) return false;
            if(o[1] < t[1]) return false;
            if(o[1] != t[1] && o[1] < 3) return false;
        }

        return true;
    }
}
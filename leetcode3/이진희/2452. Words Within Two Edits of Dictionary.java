/*

1. 아이디어 : querys의 문자열을 2번 이하로 수정해서 dictionary의 문자열 중 하나를 만들 수 있다면 ans 배열에 삽입
             모든 문제열을 완전탐색해서 진행
             가지치기를 위해 문자열이 3글자 이상 차이가 나거나, 2개 이하로 수정 가능한 문자열을 찾았으면 바로 return

2. 시간복잡도 : O(N*M*L) -> N: 쿼리 크기, M: 딕셔너리 크기, L: 각 문자열 길이(공통)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public List<String> twoEditWords(String[] queries, String[] dictionary) {
        // 최대 2번 수정해서 순서까지 유지
        // 각 i번째 쿼리와 딕셔너리 길이가 같음을 보장
        // 최대 배열 크기 100
        // 100*100 -> 1000000

        List<String> ans = new ArrayList<>();

        for(int i=0; i<queries.length; i++) {
            for(int j=0; j<dictionary.length; j++) {
                if(canEditWord(queries[i], dictionary[j])) {
                    ans.add(queries[i]);
                    break;
                }
            }
        }    

        return ans;   
    }

    private boolean canEditWord(String q, String d) {
        int cnt = 0;
        for(int i=0; i<q.length(); i++) {
            if(q.charAt(i) != d.charAt(i)) cnt++;
            if(cnt == 3) return false;
        }
        return true;
    }
}
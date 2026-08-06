/* 1차 풀이

1. 아이디어 : 문자열을 공백기준으로 파싱 후, Set에 미리 저장해놓은 dictionary에서 가장 짧은 문자열 있는지 확인후, 있다면 문자열 교체

2. 시간복잡도 : O(S*L^2)

3. 자료구조/알고리즘 : 문자열 계산 , Set

 */

class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        // 딕셔너리 포함 단어로 교체, 여러개면 더 짧은걸로
        // 최대 문장길이 100만
        
        String[] words = sentence.split(" ");
        Set<String> set = new HashSet<>();

        for(int i=0; i<dictionary.size(); i++) {
            set.add(dictionary.get(i));
        }

        StringBuilder ans = new StringBuilder();

        // 최대 10만 길이 dictionary
        for(int word=0; word<words.length; word++) {
            StringBuilder sb = new StringBuilder();
            String s = words[word];
            for(int i=0; i<s.length(); i++) {
                sb.append(s.charAt(i));
                if(set.contains(sb.toString())){
                    words[word] = sb.toString();
                    break;
                }
            }
            ans.append(words[word]).append(' ');
        }

        return ans.toString().substring(0, ans.length()-1);
    }
}
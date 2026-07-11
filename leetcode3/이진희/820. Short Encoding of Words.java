/*

1. 아이디어 :
                각 단어가 다른 단어의 접미사인지 확인
                현재 단어가 다른 단어의 접미사라면 별도로 인코딩할 필요가 없음
                두 단어의 뒤쪽 문자부터 직접 비교하여 접미사 여부를 판단
                접미사가 아닌 단어만 단어 길이와 '#'의 길이 1을 더한다

2. 시간복잡도 : O(N^2 × L) (N: 단어의 개수, L: 단어의 최대 길이)
자료구조/알고리즘 : 완전 탐색

*/

class Solution {
    public int minimumLengthEncoding(String[] words) {
        int answer = 0;

        for (int i = 0; i < words.length; i++) {
            boolean isSuffix = false;

            for (int j = 0; j < words.length; j++) {
                if (i == j) continue;

                int len1 = words[i].length();
                int len2 = words[j].length();

                if (len1 > len2) continue;

                boolean same = true;

                for (int k = 1; k <= len1; k++) {
                    char c1 = words[i].charAt(len1 - k);
                    char c2 = words[j].charAt(len2 - k);

                    if (c1 != c2) {
                        same = false;
                        break;
                    }
                }

                if (same) {
                    if (len1 == len2 && i < j) {
                        continue;
                    }

                    isSuffix = true;
                    break;
                }
            }

            if (!isSuffix) answer += words[i].length() + 1;
        }

        return answer;
    }
}
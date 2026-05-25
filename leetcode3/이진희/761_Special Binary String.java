/*

1. 아이디어 : 특별한 이진 문자열을 분리하여, 가장 크도록 정렬해야 함
            이때 1과 0의 개수는 같아야함, 입력은 항상 특별한 이진 문자열이 주어짐 (1 <= s.length <= 50 이지만 1은 나올 수 없음)
            1100 -> (()) 식으로 생각하고, (()(())) -> ((())()) 처럼 더 크기가 큰 이진 문자열이 큰 값이 앞에 오면 된다
            재귀를 활용해, 특별한 이진문자열 덩어리로 묶어, 정렬 후 최종적으로 모두 붙인 값을 반환

2. 시간복잡도 : O(N^2) + O(N^2logN) => O(N^2logN)

3. 자료구조/알고리즘 : 재귀, 문자열

 */

class Solution {
    public String makeLargestSpecial(String s) {
        if(s.length() == 2) return s;
        
        List<String> specialStr = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int count = 0;

        for(int i=0; i<s.length(); i++) {
            int n = s.charAt(i)-'0';
            if(n == 1) count++;
            else count--;

            sb.append(s.charAt(i));
            if(count == 0) {
                String innoSorted = makeLargestSpecial(sb.substring(1,sb.length()-1));
                specialStr.add("1" + innoSorted + "0");
                sb.setLength(0);
            }
        }

        Collections.sort(specialStr, Collections.reverseOrder());
        StringBuilder ans = new StringBuilder();
        for(String a : specialStr) ans.append(a);

        return ans.toString();
    }
}
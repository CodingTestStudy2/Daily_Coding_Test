/*

1. 아이디어 : 조건에 적힌대로 계산

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 구현

 */

class Solution {
    public int[] scoreValidator(String[] events) {
        int score = 0;
        int counter = 0;

        for(int i=0; i<events.length; i++) {
            String s = events[i];

            if (s.equals("W")) {
                counter++;
                if(counter == 10) break;
            } 
            else if (s.equals("WD") || s.equals("NB")) score++;
            else score+= Integer.valueOf(s); 
        }

        return new int[]{score, counter};
    }
}
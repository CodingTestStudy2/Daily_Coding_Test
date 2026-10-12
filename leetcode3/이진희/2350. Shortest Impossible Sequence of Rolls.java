/*
1. 아이디어: 풀이법을 고민하다가 AI에게 질문
           핵심은 1부터 k크기의 모든 배열에서 존재하지 않는 배열의 최소길이를 구하기 

           이때 모든 경우의 수는 구할수 없음 (최대 사이즈 10000)
           
           그렇다면 모든 배열이 존재 가능한 조건을 판단 
           1 ~ k 개의 원소가 모두 존재하는 범위를 기준으로 배열을 나누면 최소 길이 판단 가능 

           ex) 1 1 3 3 2 || 1 3  k = 3
           위 나눠진 경우를 보면 완전한 배열 1개와 숫자가 1개 부족한 배열 존재 
           
           완성된 구간에서는 모든 숫자 중 하나를 선택할 수 있고,
           마지막 미완성 구간에는 반드시 없는 숫자가 존재한다.

2. 시간복잡도: O(N)

3. 자료구조/알고리즘: 그리디
*/

class Solution {
    public int shortestSequence(int[] rolls, int k) {
        // k면체 주사위 n번 굴리기

        int ans = 0;
        int sum = 0;

        boolean[] check = new boolean[k+1];

        for(int i=0; i<rolls.length; i++) {
            int nums = rolls[i];

            if(check[nums]) continue;
            
            check[nums] = true;

            sum++;

            if(sum == k) {
                ans++;
                sum = 0;
                check = new boolean[k+1];
            }
        } 

        return ans+1;

    }
}
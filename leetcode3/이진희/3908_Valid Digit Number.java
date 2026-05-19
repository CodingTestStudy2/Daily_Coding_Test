/*

1. 아이디어 : 조건대로 풀이

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 구현

 */

class Solution {
    public boolean validDigit(int n, int x) {
        if(isValid(n,x)) return true;
        else return false;
    }

    static boolean isValid(int n, int x) {
        if(n == 0) return false;

        List<Integer> list = new ArrayList<>();

        while(n>0) {
            list.add(n%10);
            n/=10;
        }

        int firstNum = list.get(list.size()-1);
        if(firstNum == x) return false;
        if(list.contains(x)) return true;
        
        return false;
    }
}
/*

1. 아이디어 : 시키는대로 조건문을 만들면 된다

2. 시간복잡도 : O(1)

3. 자료구조/알고리즘 : 단순 조건문

 */

class Solution {
    public String trafficSignal(int timer) {
        if(timer == 0) return "Green";
        else if(timer == 30) return "Orange";
        else if(timer > 30 && timer <= 90) return "Red";
        else return "Invalid";
    }
}
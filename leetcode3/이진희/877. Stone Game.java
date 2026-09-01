/*

1. 아이디어 : 짝수개의 돌, 돌의 총 개수는 홀수
              A->B로 번갈아가며 돌을 선택하고 이때 양끝 돌 중 하나를 선택
              
              A가 이기면 true, B가 이기면 false

              순서가 A부터 고정되고 가져가는 돌의 위치도 정해져 있어, 생각해보면 A는 항상 이길 수 있다.


2. 시간복잡도 : O(1)
자료구조/알고리즘 : 아이디어

*/

class Solution {
    public boolean stoneGame(int[] piles) {
        // A -> B
        // 맨 앞과 맨 끝 중 돌 가져가기

        // int l = 0;
        // int r = piles.length-1;
        // int a = 0;
        // int b = 0;

        // while(l<r) {
        //     // A
        //     if(piles[l]>=piles[r]) {
        //         a+=piles[l];
        //         l++;
        //     }
        //     else {
        //         a+=piles[r];
        //         r--;
        //     }

        //     // B
        //     if(piles[l]>piles[r]) {
        //         b+=piles[r];
        //         r--;
        //     }
        //     else {
        //         b+=piles[l];
        //         l++;
        //     }
        // }

        // return a>b;

        return true;
    }
}
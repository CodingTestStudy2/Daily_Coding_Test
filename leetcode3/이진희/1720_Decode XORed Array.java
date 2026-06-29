/*

1. 아이디어 : XOR 연산의 성질(A ^ B = C 이면 A ^ C = B)을 활용하여 복원

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 비트 연산 (XOR)

*/

class Solution {
    public int[] decode(int[] encoded, int first) {
        int[] arr = new int[encoded.length + 1];
        
        arr[0] = first;
        
        for (int i = 0; i < encoded.length; i++) {
            arr[i + 1] = encoded[i] ^ arr[i];
        }
        
        return arr;
    }
}
/*
1. 아이디어: 포인터를 이동하며 1을 만나면 2칸, 0을 만나면 1칸 이동 -> 마지막 인덱스에 정확히 도달하는지 확인

2. 시간복잡도: O(N)

3. 자료구조/알고리즘: 시뮬레이션

*/

class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0;
        int len = bits.length;
        
        while (i < len - 1) {
            if (bits[i] == 1)  i += 2;
            else i += 1;
        }    
        return i == len - 1;
    }
}
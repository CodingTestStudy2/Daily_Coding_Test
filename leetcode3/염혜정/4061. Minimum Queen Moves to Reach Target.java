// O(1)

class Solution {
    public int minQueenMoves(int[] source, int[] target) {
        int x = Math.abs(source[0]-target[0]);
        int y = Math.abs(source[1]-target[1]);

        if (x == 0 && y == 0) return 0;
        else if (x == 0 || y == 0 || x == y) return 1;
        else return 2;
    }
}

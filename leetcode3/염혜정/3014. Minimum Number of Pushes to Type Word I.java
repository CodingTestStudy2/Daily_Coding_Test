// O(n)

class Solution {
    public int minimumPushes(String word) {
        int cnt = word.length()/8;
        int min = (word.length() % 8) * (cnt + 1);
        int i = 1;
        while (cnt > 0) {
            min += (8 * i);
            i++;
            cnt--;
        }
        return min;
    }
}

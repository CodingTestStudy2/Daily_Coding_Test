// O(n)...

class Solution {
    public int findKthPositive(int[] arr, int k) {
        Set<Integer> set = new HashSet<>();
        for (int a : arr) set.add(a);
        
        int i = 1;
        int cnt = 0;
        int result = 0;
        while(true) {
            if (!set.contains(i)) cnt++;
            if (cnt == k) {
                result = i;
                break;
            }
            i++;
        }
        return result;
    }
}

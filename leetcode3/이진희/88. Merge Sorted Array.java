import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int idx1 = 0;
        int idx2 = 0;
        Deque<Integer> dq = new ArrayDeque<>();

        for (int i = 0; i < m; i++) {
            dq.add(nums1[i]);
        }

        for (int i = 0; i < m + n; i++) {
            if (!dq.isEmpty() && idx2 < n) {
                if (dq.peek() <= nums2[idx2]) {
                    nums1[i] = dq.poll();
                } else {
                    nums1[i] = nums2[idx2];
                    idx2++;
                }
            } else if (!dq.isEmpty()) {
                nums1[i] = dq.poll();
            } else {
                nums1[i] = nums2[idx2];
                idx2++;
            }
        }
    }
}
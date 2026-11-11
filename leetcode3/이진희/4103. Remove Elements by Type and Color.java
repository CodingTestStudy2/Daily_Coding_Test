class Solution {
    public boolean canRemoveAll(int[] types, int[] colors, int[] groupSize) {
        Deque<int[]> dq = new ArrayDeque<>();

        for (int i = 0; i < types.length; i++) {
            int t = types[i];
            int c = colors[i];
            
            if (groupSize[t] == 1) continue; 

            if (!dq.isEmpty() && dq.peekLast()[0] == t && dq.peekLast()[1] == c) {
                int[] top = dq.pollLast();
                int nextCnt = top[2] + 1;
                
                if (nextCnt < groupSize[t]) dq.addLast(new int[]{t, c, nextCnt});
            } else {
                dq.addLast(new int[]{t, c, 1});
            }
        }

        return dq.isEmpty();
    }
}
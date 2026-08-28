// O(3n)

class Solution {
    public int nearestDrone(int[][] drones, int[] target) {
        int x = target[0];
        int y = target[1];
        int min = Integer.MAX_VALUE;
        int idx = 0;
        for (int i = 0; i<drones.length; i++) {
            int md = Math.abs(drones[i][0]-x) + Math.abs(drones[i][1]-y);
            if (md > drones[i][2]) continue;
            if (md < min) {
                min = md;
                idx = i;
            }
        }
        if (min == Integer.MAX_VALUE) return -1;
        return idx;
    }
}

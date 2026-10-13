// 커스텀 정렬
// O(n log n)

class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int[][] events = new int[trips.length*2][2];
        int i = 0;
        for (int[] trip : trips) {
            events[i] = new int[]{trip[1], trip[0]};
            i++;
            events[i] = new int[]{trip[2], -trip[0]};
            i++;
        }

        Arrays.sort(events, (a, b) -> {
            // 승차 + 하차 -
            // 위치 오름차순, 위치가 같으면 승객 오름차순
            if (a[0] == b[0]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[0], b[0]);
        });

        int now = 0;
        for (int[] event : events) {
            now += event[1];
            if (now > capacity) return false;
        }
        return true;
    }
}

/*
 * TreeMap<구간 시작, 구간 끝> 으로 disjoint 구간 유지
 *  - floorKey(value): value 이하로 시작하는 가장 가까운 구간 (왼쪽 후보)
 *  - ceilingKey(value): value 이상으로 시작하는 가장 가까운 구간 (오른쪽 후보)
 *    1. 이미 왼쪽 구간에 포함  -> 무시
 *    2. 양쪽 모두 인접(좌 끝==v-1, 우 시작==v+1) -> 두 구간을 하나로 병합
 *    3. 왼쪽만 인접 -> 왼쪽 구간 끝을 v로 확장
 *    4. 오른쪽만 인접 -> 오른쪽 구간 시작을 v로 당김
 *    (아무데도 안 붙으면 [v,v] 새 구간 생성)
 *  addNum: O(log n) / getIntervals: O(n)
 */

class SummaryRanges {
    private TreeMap<Integer, Integer> intervals;

    public SummaryRanges() {
        intervals = new TreeMap<>();
    }

    public void addNum(int value) {
        Integer lo = intervals.floorKey(value);
        Integer hi = intervals.ceilingKey(value);

        if (lo != null && intervals.get(lo) >= value) return;

        boolean mergeLeft  = (lo != null && intervals.get(lo) == value - 1);
        boolean mergeRight = (hi != null && hi == value + 1);

        if (mergeLeft && mergeRight) {          
            intervals.put(lo, intervals.get(hi));
            intervals.remove(hi);
        } else if (mergeLeft) {                
            intervals.put(lo, value);
        } else if (mergeRight) {               
            intervals.put(value, intervals.get(hi));
            intervals.remove(hi);
        } else {                               
            intervals.put(value, value);
        }
    }

    public int[][] getIntervals() {
        int[][] res = new int[intervals.size()][2];
        int i = 0;
        for (Map.Entry<Integer, Integer> e : intervals.entrySet()) {
            res[i][0] = e.getKey();
            res[i++][1] = e.getValue();
        }
        return res;
    }
}

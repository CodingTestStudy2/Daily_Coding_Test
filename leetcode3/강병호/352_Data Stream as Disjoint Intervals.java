import java.util.TreeMap;

class SummaryRanges {
    private TreeMap<Integer, int[]> treeMap;

    public SummaryRanges() {
        treeMap = new TreeMap<>();
    }
    
    public void addNum(int value) {
        Integer floorKey = treeMap.floorKey(value);
        Integer ceilingKey = treeMap.ceilingKey(value);

        if (floorKey != null) {
            int[] leftInterval = treeMap.get(floorKey);
            if (leftInterval[1] >= value) {
                return; 
            }
        }

        boolean mergeLeft = (floorKey != null && treeMap.get(floorKey)[1] + 1 == value);
        boolean mergeRight = (ceilingKey != null && ceilingKey == value + 1);

        if (mergeLeft && mergeRight) {
            treeMap.get(floorKey)[1] = treeMap.get(ceilingKey)[1];
            treeMap.remove(ceilingKey);
        } else if (mergeLeft) {
            treeMap.get(floorKey)[1] = value;
        } else if (mergeRight) {
            int[] rightInterval = treeMap.remove(ceilingKey);
            rightInterval[0] = value;
            treeMap.put(value, rightInterval);
        } else {
            treeMap.put(value, new int[]{value, value});
        }
    }
    
    public int[][] getIntervals() {
        return treeMap.values().toArray(new int[treeMap.size()][]);
    }
}
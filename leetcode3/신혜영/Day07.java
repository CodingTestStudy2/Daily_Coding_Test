import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Day07  {
    public static List<List<Long>> splitPainting(int[][] segments) {
        Map<Integer, Long> change = new TreeMap<>();

        for (int i = 0; i < segments.length; i++) {
            int start = segments[i][0];
            int end = segments[i][1];
            int color = segments[i][2];
            change.put(start, change.getOrDefault(start, 0L) + color);
            change.put(end, change.getOrDefault(end, 0L) - color);
        }

        List<List<Long>> answer = new ArrayList<>();
        long currentSum = 0;
        long prev = 0;

        for (int curr : change.keySet()) {
            if (prev != 0 && currentSum > 0) {
                answer.add(Arrays.asList(prev, (long)curr, currentSum));
            }

            currentSum += change.get(curr);
            prev = curr;
        }

    }

    public static void main(String[] args) {
        int[][] test = {{1,4,5},{1,7,7}};

        splitPainting(test);
    }
}

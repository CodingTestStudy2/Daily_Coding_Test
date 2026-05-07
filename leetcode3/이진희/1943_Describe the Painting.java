/*

1. 아이디어 : 모든 구간을 더하는건 불가. start와 end를 기준으로 계산한다
            오름차순 정렬이 되는 TreeMap을 사용해, 각 좌표와 좌표기준 색을 기록한다
            이때, 시작지점은 색을 더하고, 끝 지점은 색을 뺀다
            이후 누적합을 사용해 0보다 값이 크다면, 결과에 기록한다

2. 시간복잡도 : O(NlogN) + O(N) + O(N) 

3. 자료구조/알고리즘 : TreeMap(차분배열) + 누적합

 */
class Solution {
    public List<List<Long>> splitPainting(int[][] segments) {
        TreeMap<Long, Long> map = new TreeMap<>();
        
        for(int[] segment : segments){
            long start = segment[0];
            long end = segment[1];
            long color = segment[2];

            if(map.containsKey(start)) map.put(start, map.get(start) + color);
            else map.put(start, color);

            if(map.containsKey(end)) map.put(end, map.get(end) - color);
            else map.put(end, -color);
        }

        List<List<Long>> ans = new ArrayList<>();
        long currSum = 0L;
        long prePos = -1;

        // 오름차 순
        for(long currPos : map.keySet()) {
            if(prePos != -1 && currSum > 0) {
                ans.add(Arrays.asList(prePos,currPos,currSum));
            }
            currSum+=map.get(currPos);
            prePos = currPos;
        }

        return ans;
    }
}
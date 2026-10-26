/*
1. 아이디어:
   - 모든 꽃을 피우는 가장 짧은 일 수 계산
   - 꽃을 심는 기간동안 다른 꽃을 같이 심을수 없다. 
   - 그러므로 plantTime은 고정되고 growTime에 따라 기간이 결정
   - growTime이 길수록 먼저 심는게 유리하므로 growTime이 높은순으로 정렬 후 값을 계산한다

2. 시간복잡도: O(N)

3. 자료구조/알고리즘: 그리디
*/

class Solution {
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        // 1. 꽃을 심는 작업은 겹칠 수 없다
        // 2. 꽃은 growTime+1에 핀다
        // 3. 꽃을 나눠 심어도 된다

        List<int[]> flowers = new ArrayList<>();

        for(int i=0; i<plantTime.length; i++) {
            flowers.add(new int[]{plantTime[i], growTime[i]});
        }

        Collections.sort(flowers, (a,b) -> Integer.compare(b[1],a[1]));

        int allBloomingPeriod = flowers.get(0)[0];
        int nextBlooming = flowers.get(0)[1]+1;

        for(int i=1; i<plantTime.length; i++) {
            int p = flowers.get(i)[0];
            int g = flowers.get(i)[1]+1;

            allBloomingPeriod += p;
            nextBlooming = Math.max(nextBlooming-p, g);
        }

        return allBloomingPeriod + nextBlooming -1;
    }
}
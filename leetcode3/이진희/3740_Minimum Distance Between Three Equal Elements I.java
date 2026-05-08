/* 2차 해결

1. 아이디어 : 수식을 2*(k-i)로 간소화, 맨 처음과 맨끝 점 사이의 거리만 갱신

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 슬라이딩 윈도우

 */

class Solution {
    public int minimumDistance(int[] nums) {
        //j-i+k-j+k-i = 2*(k-i)
        int[] start = new int[101];
        int[] end = new int[101];
        
        int sum = Integer.MAX_VALUE;

        Arrays.fill(start, -1);
        Arrays.fill(end, -1);

        for(int i=0; i<nums.length; i++) {
            int n = nums[i];

            if(start[n] == -1) start[n] = i;
            else if(end[n] == -1) end[n] = i;
            else {
                sum = Math.min(sum, 2*(i-start[n]));
                start[n] = end[n];
                end[n] = i;
            }
        }

        if(sum == Integer.MAX_VALUE) return -1;
        else return sum;
    }
}

/* 1차 해결

1. 아이디어 : 이중 리스트를 만들어, 최대 100개의 값 초기화
            이후 인덱스마다 값을 저장 후, 다시 값단위로 꺼내어 정렬
            정렬한 숫자에서 최솟값을 구한다

2. 시간복잡도 : O(N)(입력) + O(NlogN)(정렬) + O(N)(거리 계산) => O(NlogN)

3. 자료구조/알고리즘 : 단순계산

 */
class Solution {
    public int minimumDistance(int[] nums) {

        return findMinSum(nums);
    }

    //최소 거리 3
    static int findMinSum(int[] nums) {
        List<List<Integer>> arr = new ArrayList<>();
        for(int i=0; i<=100; i++) arr.add(new ArrayList<>());

        boolean isGood = false;
        for(int i=0; i<nums.length; i++){
            arr.get(nums[i]).add(i);
            if(!isGood && arr.get(nums[i]).size() > 2) isGood = true;
        }

        if(!isGood) return -1;
        int minDist = Integer.MAX_VALUE;
        
        for(List<Integer> list : arr) {
            if(list.size() < 3) continue;
            Collections.sort(list);
            for(int i=0; i<list.size()-2; i++){
                int a = list.get(i);
                int b = list.get(i+1);
                int c = list.get(i+2);
                minDist = Math.min(minDist, 2*(c-a));
                if(minDist == 3) return 3;
            }
        }

        return minDist;
    }
}
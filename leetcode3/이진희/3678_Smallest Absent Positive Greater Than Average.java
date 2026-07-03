/* 2차 풀이

1. 아이디어 : Set사용, 미리 포함된 배열의 값을 저장, while문으로 값을 1씩 올려가며 찾는다
              이때, 답은 양수만 되고, 값이 무조건 평균값보다 커야함에 주의

2. 시간복잡도 : O(N + 배열 평균값 ~ 배열의 가장 큰 수+1)

3. 자료구조/알고리즘 : Set

 */

class Solution {
    public int smallestAbsent(int[] nums) {
        // 가장 작은 nums 배열에 없는 양수 찾기
        // 배열 합의 평균값보다 무조건 커야함

        double sum = 0.0;
        Set<Integer> set = new HashSet<>();

        for(int i=0; i<nums.length; i++) {
            sum+=nums[i];
            set.add(nums[i]);
        } 

        sum/=nums.length;
        int ans = sum>0 ? (int)sum : 1;

        while(true) {
            if(ans>sum && !set.contains(ans)) return ans;
            ans++;
        }
    }
}

/* 1차 풀이

1. 아이디어 : Set사용, 배열의 수를 미리 저장 후, 평균을 구한 뒤, 값을 1씩 올려가며 찾는다

2. 시간복잡도 : O(2N)

3. 자료구조/알고리즘 : Set

 */


class Solution {
    public int smallestAbsent(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int sum = 0;
        
        for (int num : nums) {
            set.add(num);
            sum += num;
        }
        
        int start = sum / nums.length + 1;
        
        int ans = Math.max(1, start);
        
        while (set.contains(ans)) ans++;
        
        return ans;
    }
}
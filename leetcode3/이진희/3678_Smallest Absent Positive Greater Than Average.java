/*

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
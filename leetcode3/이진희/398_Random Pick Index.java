/*

1. 아이디어 : 시키는 조건대로 함수 구현
            1. Solution 객체 초기화
            2. 특정 숫자의 index 출력, 그 숫자가 여러개일경우 같은 확률로 랜덤 index 출력

            Random 함수를 사용해야하고, Map을 사용하여 각 숫자의 위치를 기록 -> 최대 2만이라 가능

            // 아래 문제는 공간, 시간복잡도를 O(N)으로 해결해야함
            유사문제: https://leetcode.com/submissions/detail/2022970405/

2. 시간복잡도 : 1. Solution 함수 -> O(N)
             2. pick 함수 -> O(1)

3. 자료구조/알고리즘 : Map, Random 함수

 */

class Solution {
    //최대 2만
    private Random random;
    private Map<Integer, List<Integer>> map;


    // nums 초기화
    public Solution(int[] nums) {
        random = new Random();
        map = new HashMap<>();

        for(int idx=0; idx<nums.length; idx++) {
            if(map.containsKey(nums[idx])) map.get(nums[idx]).add(idx);
            else {
                map.put(nums[idx], new ArrayList<>());
                map.get(nums[idx]).add(idx);
            }
        }
    }
    
    // nums[i] == target
    // 여러가지면 랜덤 출력
    // 반드시 존재
    public int pick(int target) {
        int size = map.get(target).size();
        return map.get(target).get(random.nextInt(size));
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
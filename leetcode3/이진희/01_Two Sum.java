/*

1. 아이디어 : 
    1차(투포인터): 2차원 배열로 (값, 인덱스) 함께 저장 후 정렬하여 탐색. O(NlogN) + O(N)
    2차(HashMap): 값:key, 인덱스:값 -> target을 만들기 위해 필요한 나머지 숫자 검색. O(N)

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : HashMap

 */

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<>();
        
        for(int i=0; i<nums.length; i++) {
            int addNum = target-nums[i];

            if(map.containsKey(addNum)) return new int[]{map.get(addNum), i};

            map.put(nums[i], i);
        }
        return new int[]{-1,-1};
    }
}
/*

1. 아이디어 : 초반 SWAP으로 각 위치를 교환하려고 했으나 예외케이스가 늘어나 실패 
             추가 공간 복잡도를 활용할 수 없고 각 nums[i]의 범위가 1<=nums[i]<=n인것을 바탕으로 숫자를 만났을때 음수를 붙여 이미 본 적있는지 체크

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 부호 반전

 */

class Solution {
    // 각 원소는 최대 두 번 등장
    // 시간복잡도 O(N)
    // 추가 공간은 배열의 크기에 따라가 변하지 않고 고정적이어야 함
    // 답을 위한 추가 공간 제외
    // 두번 등장하는 모든 윈소를 출력 (출력 순서는 상관 없음)
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer>ans = new ArrayList<>();

        for(int i=0; i<nums.length; i++) {
            int num = Math.abs(nums[i]);

            if(nums[num-1] < 0) ans.add(num);
            else nums[num-1] = -nums[num-1];
        }

        return ans;
    }
}
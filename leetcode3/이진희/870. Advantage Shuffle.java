/* 

1. 아이디어 : nums1[i]>nums2[i]를 만족하는 최대 원소를 가진 아무 배열 반환
              nums1, nums2배열을 정렬후, 투 포인터로 위 조건을 만족하는 최대 원소 배열을 구함
              이때 nums2의 원소 위치를 미리 저장해놔야한다.

2. 시간복잡도 : O(2NlogN + N) => O(NlogN)

3. 자료구조/알고리즘 : 투포인터, 커스텀 정렬

 */

class Solution {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        // 최대한 많은 원소가 nums1[i] > nums2[i]를 만족

        // 2 7 11 15
        // 8 12 24 32

        Arrays.sort(nums1);
        List<int[]> nums2Idx = new ArrayList<>();
        for(int i=0; i<nums2.length; i++) nums2Idx.add(new int[]{i,nums2[i]});

        Collections.sort(nums2Idx, (a,b) ->{
            return a[1]-b[1];
        });

        int[] ans = new int[nums1.length];

        // 2 7 11 15
        // 1 4 10 11

        // 8 12 24 32
        // 11 13 25 32

        int r = nums2.length-1;
        int l = 0;

        for(int i=nums2.length-1; i>=0; i--) {
            int num = nums2Idx.get(i)[1];
            int pos = nums2Idx.get(i)[0];

            if(nums1[r]>num) {
                ans[pos] = nums1[r];
                r--;
            }
            else {
                ans[pos] = nums1[l];
                l++;
            }
        }

        return ans;

    }
}
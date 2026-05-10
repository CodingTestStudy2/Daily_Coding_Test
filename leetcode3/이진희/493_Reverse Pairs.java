/* 

1. 아이디어 : 분할정복을 사용하여 문제 풀이
            최대 50만 크기의 배열이고, 특정 범위의 모든 수를 구해야함
            병합 정렬 과정에서 왼쪽, 오른쪽 그룹으로 나뉘고, 이때 왼쪽 그룹 인덱스는 항상 오른쪽보다 작음
            또한 그룹이 정렬되어 있다면, 투포인터로 조건에 맞는 개수를 쉽게 구할 수 있음
                (한 숫자가 조건을 만족하면 그 이상의 숫자도 당연히 만족하게 되므로)

2. 시간복잡도 : O(NlongN)

3. 자료구조/알고리즘 : 병합정렬 구현 + 투포인터

 */

class Solution {
    public int reversePairs(int[] nums) {
        if (nums.length == 1) return 0;
        return divide(nums, 0, nums.length - 1);
    }

    private int divide(int[] nums, int left, int right) {
        if(left >= right) return 0;

        int mid = left + (right - left) / 2;
        int count = 0;

        count += divide(nums, left, mid);
        count += divide(nums, mid+1, right);
        
        count += countPairs(nums, left, mid, right);
        merge(nums, left, mid, right);

        return count;
    }

    private int countPairs(int[] nums, int left, int mid, int right) {
        int res = 0;
        int r = mid+1;

        for (int l = left; l <= mid; l++) {
            while(r <= right) {
                long leftV = (long) nums[l];
                long rightV = (long) nums[r];

                if(leftV > 2*rightV) r++;
                else break;
            }

            int count = r - (mid+1);
            res += count;
        }

        return res;
    }

    private void merge(int[] nums, int left, int mid, int right) {
        int[] tmp = new int[right - left +1];
        int leftIdx = left;
        int rightIdx = mid+1;
        int tmpIdx = 0;

        while (leftIdx <= mid && rightIdx <= right) {
            if(nums[leftIdx] <= nums[rightIdx]) tmp[tmpIdx++] = nums[leftIdx++];
            else tmp[tmpIdx++] = nums[rightIdx++];
        }

        while (leftIdx <= mid) tmp[tmpIdx++] = nums[leftIdx++];
        while (rightIdx <= right) tmp[tmpIdx++] = nums[rightIdx++];

        for(int i=0; i<tmp.length; i++) nums[left + i] = tmp[i];
    }
}
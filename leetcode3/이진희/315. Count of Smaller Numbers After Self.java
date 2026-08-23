/*

1. 아이디어 : 머지 소트 방식 활용. 병합정렬중 Merge 단계에서, 왼쪽 배열의 값이 오른쪽 배열의 값보다 크다면, 
             오른쪽 배열의 값이 왼쪽 배열의 값보다 작다는 의미이므로, count를 증가시킨다

2. 시간복잡도 : O(NlogN)

3. 자료구조/알고리즘 : 머지소트

 */

class Solution {
    private int[] count;

    private class Pair {
        int val;
        int index;

        Pair(int val, int index) {
            this.val = val;
            this.index = index;
        }
    }

    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        count = new int[n];
        
        Pair[] pairs = new Pair[n];
        for (int i = 0; i < n; i++) {
            pairs[i] = new Pair(nums[i], i);
        }

        mergeSort(pairs, 0, n - 1);

        List<Integer> result = new ArrayList<>();
        for (int c : count) {
            result.add(c);
        }
        return result;
    }

    private void mergeSort(Pair[] pairs, int left, int right) {
        if (left >= right) return;

        int mid = left + (right - left) / 2;
        mergeSort(pairs, left, mid);
        mergeSort(pairs, mid + 1, right);

        merge(pairs, left, mid, right);
    }

    private void merge(Pair[] pairs, int left, int mid, int right) {
        Pair[] temp = new Pair[right - left + 1];
        int i = left;
        int j = mid + 1;
        int k = 0;
        int rightCount = 0;

        while (i <= mid && j <= right) {
            if (pairs[j].val < pairs[i].val) {
                rightCount++;
                temp[k++] = pairs[j++];
            } else {
                count[pairs[i].index] += rightCount;
                temp[k++] = pairs[i++];
            }
        }

        while (i <= mid) {
            count[pairs[i].index] += rightCount;
            temp[k++] = pairs[i++];
        }

        while (j <= right) {
            temp[k++] = pairs[j++];
        }

        System.arraycopy(temp, 0, pairs, left, temp.length);
    }
}
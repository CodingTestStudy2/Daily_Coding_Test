/*

1. 아이디어 : 
   - 리스트가 오름차순으로 정렬될 때까지 반복
   - 인접한 두 원소의 합이 가장 최소가 되는 위치 찾기
   - 해당 위치의 두 원소를 합치고 카운트 증가

2. 시간복잡도 : O(N^2)

3. 자료구조/알고리즘 : 시뮬레이션

 */

class Solution {
    public int minimumPairRemoval(int[] nums) {
        List<Integer> list = new ArrayList<>();

        for (int num : nums) {
            list.add(num);
        }

        int cnt = 0;

        while (true) {
            boolean sorted = true;

            for (int i = 0; i < list.size() - 1; i++) {
                if (list.get(i) > list.get(i + 1)) {
                    sorted = false;
                    break;
                }
            }

            if (sorted) {
                break;
            }

            int minIndex = 0;
            int minSum = list.get(0) + list.get(1);

            for (int i = 1; i < list.size() - 1; i++) {
                int sum = list.get(i) + list.get(i + 1);

                if (sum < minSum) {
                    minSum = sum;
                    minIndex = i;
                }
            }

            list.set(minIndex, minSum);
            list.remove(minIndex + 1);

            cnt++;
        }

        return cnt;
    }
}
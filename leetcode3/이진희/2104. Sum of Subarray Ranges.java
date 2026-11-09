/* 2차 풀이

1. 아이디어 : 각 구간의 최대 최소를 각각 계산하는게 아닌 최대값 합 - 최솟값 합으로 계산 
             각 idx 기준 좌,우로 최대 최소를 만족하는 구간 인덱스를 스택에 저장
             값이 갱신될때마다 허용 가능한 범위내에서 중복으로 나온다는 의미이므로 nums[idx]*구간길이의 합을 누적
             최종 결과는 max값의 누적 - min값의 누적

2. 시간복잡도 : O(2*N)

3. 자료구조/알고리즘 : 스택 성질 활용

*/

class Solution {
    public long subArrayRanges(int[] nums) {
        int n = nums.length;
        long sumMax = 0;
        long sumMin = 0;
        
        Deque<Integer> minStack = new ArrayDeque<>();
        Deque<Integer> maxStack = new ArrayDeque<>();

        for (int i=0; i<n; i++) {
            while (!minStack.isEmpty() && nums[minStack.peek()] > nums[i]) {
                int mid = minStack.pop();
                
                int left = -1;
                if (!minStack.isEmpty()) left = minStack.peek();
                int right = i;
                
                sumMin += (long) nums[mid]*(mid-left)*(right-mid);
            }
            while (!maxStack.isEmpty() && nums[maxStack.peek()] < nums[i]) {
                int mid = maxStack.pop();
                
                int left = -1;
                if (!maxStack.isEmpty()) left = maxStack.peek();
                int right = i;
                
                sumMax += (long) nums[mid]*(mid-left)*(right-mid);
            }
            maxStack.push(i);
            minStack.push(i);
        }

        while (!minStack.isEmpty()) {
            int mid = minStack.pop();
            
            int left = -1;
            if (!minStack.isEmpty()) left = minStack.peek();
            int right = n;
                        
            sumMin += (long) nums[mid]*(mid-left)*(right-mid);
        }

        while (!maxStack.isEmpty()) {
            int mid = maxStack.pop();
            
            int left = -1;
            if (!maxStack.isEmpty()) left = maxStack.peek();
            int right = n;
                        
            sumMax += (long)nums[mid]*(mid-left)*(right-mid);
        }

        return sumMax - sumMin;
    }
}

/* 1차 풀이

1. 아이디어 : 모든 구간을 탐색하면서 각 i-j구간의 최대 최소 갱신 후 계산

2. 시간복잡도 : O(N^2)

3. 자료구조/알고리즘 : 완전탐색

*/

class Solution {
    public long subArrayRanges(int[] nums) {
        long ans = 0L;
        int[][] minDP = new int[nums.length][nums.length];
        int[][] maxDP = new int[nums.length][nums.length];

        int len = nums.length;
        for(int i=0; i<len; i++) {
            minDP[i][i] = nums[i];
            maxDP[i][i] = nums[i];
        }

        for(int i=0; i<len-1; i++) {
            for(int j=i+1; j<len; j++) {
                minDP[i][j] = Math.min(minDP[i][j-1], nums[j]);
                maxDP[i][j] = Math.max(maxDP[i][j-1], nums[j]);

                ans+=maxDP[i][j] - minDP[i][j];
            }
        }

        return ans;
    }
}
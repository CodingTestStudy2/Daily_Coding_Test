/*

1. 아이디어 : 

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 투포인터

 */

class Solution {
    public int edgeScore(int[] edges) {
        long[] numSum = new long[edges.length];
        long maxSum = -1;
        int ans = -1;
        
        for(int i=0; i<edges.length; i++) {
            numSum[edges[i]] += i;
        }

        for(int i=0; i<edges.length; i++) {
            if(maxSum<numSum[i]){
                maxSum = numSum[i];
                ans = i;
            }
        }

        return ans;
    }
}
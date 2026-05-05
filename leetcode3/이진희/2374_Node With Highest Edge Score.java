/*

1. 아이디어 : 0, n-1까지의 노드 중, 본인을 가리키는 서로 다른 노드의 인덱스 합이 가장 큰 노드 구하기
           long[] 으로 n-1크기의 배열을 선언후, for문으로 계산
           이후 다시 for문으로 계산된 합을 돈 뒤, 인덱스는 가장 작되, 합이 가장 큰 노드를 구한다 

2. 시간복잡도 : O(N) + O(N) => O(N)

3. 자료구조/알고리즘 : 단순계산

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
/* 

1. 아이디어 : 실제 소모되는 에너지, 일을 시작하기위해 필요한 에너지가 각각 주어졌으므로, 최소 소모되는 에너지량을 구한다.
            처음에는 1. minimum 오름차순 -> 2. actual 오름차순으로 정렬했지만, 최소 비용을 구하기 위해서는 minimum-actual 값 기준 
            오름차순으로 배열을 정렬해야함 

            남는 에너지가 많은 일부터 처리할수록 다음 task시 에너지 보충이 적어지기 때문


2. 시간복잡도 : O(NlogN)

3. 자료구조/알고리즘 : 그리디, 커스텀 정렬

 */
class Solution {
    public int minimumEffort(int[][] tasks) {
        // 순서 상관없이 모든 일을 끝낼 수 있는 "최소"에너지

        int ans = 0;
        int currEnergy = 0;

        Arrays.sort(tasks, (a,b) -> {
            return Integer.compare(b[1]-b[0], a[1]-a[0]);
        });

        for(int i=0; i<tasks.length; i++) {
            int a = tasks[i][0];
            int m = tasks[i][1];

            int diff = currEnergy-m;

            if(diff<0) {
                ans-=diff;
                currEnergy=m;
            }

            currEnergy-=a;
        }

        return ans;
    }
}
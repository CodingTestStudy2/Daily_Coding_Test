/* 2차 풀이

1. 아이디어 : 완전탐색 + 유클리드 호제법 + 가지치기

              1차 풀이에서 모든 값을 비교하는 부분을 최적화 
              1. 내림차순 정렬 - 최댓값을 빠르게 찾기 위해
              2. 뒤부터 한 값을 기준으로 비교하며 두 값의 최대공약수가 1일경우 break - 나올 수 있는 최대 값이므로
              3. 현재 쌍(i,j)를 곱했을때 현재 최댓값보다 작아도 break - i*j/(최대공약수의 제곱) 일때 나올수 있는 최대값은 i*j므로

              1차 풀이: 1071ms Beats 12.61%
              2차 풀이: 252ms Beats 99.47%

2. 시간복잡도 : O(N^2*logL) (L은 Num중 가장 큰 값)

3. 자료구조/알고리즘 : 완전탐색 + 유클리드 호제법 + 가치치기

 */
class Solution {
    public long maxPairStrength(int[] nums) {
        long ans = 0L;

        Arrays.sort(nums);

        for(int i=nums.length-1; i>0; i--) {
            for(int j=i-1; j>=0; j--) {
                // 가지치기
                if((long)nums[i]*nums[j] <= ans) break;
                
                long cal = (long)nums[i]*nums[j];

                // 가지치기
                if(gcd(nums[i], nums[j]) == 1) {
                    ans = Math.max(ans, cal);
                    break;
                }

                ans = Math.max(ans, cal/(long)Math.pow(gcd(nums[i], nums[j]),2));
            }
        }
        return ans;
     }

     private int gcd(int a, int b) {
        if(b==0) return a;
        return gcd(b,a%b);
     }
}

/* 1차 풀이

1. 아이디어 : 완전탐색과 유클리드 호제법으로 최대공약수를 구해서 풀이 

2. 시간복잡도 : O(N^2*logL) (L은 Num중 가장 큰 값)

3. 자료구조/알고리즘 : 완전탐색 + 유클리드 호제법

 */

class Solution {
    public long maxPairStrength(int[] nums) {
        long ans = 0L;
        for(int i=0; i<nums.length-1; i++) {
            for(int j=i+1; j<nums.length; j++) {
                int cal = gcd(nums[i],nums[j]);
                ans = Math.max(ans, (long)nums[i]*nums[j] / (long)Math.pow(cal,2));
            }
        }
        return ans;
     }

     private int gcd(int a, int b) {
        if(b==0) return a;
        return gcd(b,a%b);
     }
}
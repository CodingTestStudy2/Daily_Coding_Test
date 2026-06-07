/* 

1. 아이디어 : 조건에 맞게 최소 사탕의 개수를 구해야 한다
            1. 모든 아이는 최소 1개의 사탕을 가진다
            2. rating이 높을 경우 이웃한 사람보다 더 많은 사탕을 가져야 한다

            미리 사탕을 1로 초기화해두고, 완전탐색을 순차와 역순으로 각각 돌려서 조건에 맞는 최소 사탕개수를 구한다
            이때 역순으로 한번더 탐색하는 이유는 1 2 3 4 4 4 3 2 1 일 경우, 순차 탐색을 하면 사탕 개수 파악이 한번에 어렵기 때문

2. 시간복잡도 : O(2*N)

3. 자료구조/알고리즘 : Greedy

 */

class Solution {
    public int candy(int[] ratings) {
      // 조건
      // 1. 모든 아이는 최소한 1개의 candy를 받아야 함
      // 2. 높은 등수(큰 숫자)의 아이는 이웃보다 더 많은 캔디를 받아야 함

      if(ratings.length == 1) return 1;

      if(ratings.length == 2) {
        if(ratings[0] == ratings[1]) return 2;
        else return 3;
      }

      int[] candy = new int[ratings.length];
      Arrays.fill(candy, 1);
      int ans = 0;

      for(int i=1; i<ratings.length; i++) {
        if(ratings[i-1] != ratings[i]) {
            if(ratings[i]>ratings[i-1]) {
                if(candy[i]<=candy[i-1]) candy[i]=candy[i-1]+1;
            }
            else if(ratings[i]<ratings[i-1]) {
                if(candy[i]>=candy[i-1]) candy[i-1]=candy[i]+1;
            }
        }
      }

      for(int i=ratings.length-1; i>0; i--) {
        if(ratings[i-1] != ratings[i]) {
            if(ratings[i]>ratings[i-1]) {
                if(candy[i]<=candy[i-1]) candy[i]=candy[i-1]+1;
            }
            else if(ratings[i]<ratings[i-1]) {
                if(candy[i]>=candy[i-1]) candy[i-1]=candy[i]+1;
            }
        }
      }

      for(int i: candy) ans+=i;
      
      return ans;
    }
}
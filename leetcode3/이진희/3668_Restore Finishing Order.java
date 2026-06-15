/*

1. 아이디어 : friends배열의 숫자를 Set에 저장
              order를 완전탐색하면서, friends에 그 숫자와 겹칠경우 저장
              이후, int[] 배열로 변환하여 return

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : Set

 */

class Solution {
    public int[] recoverOrder(int[] order, int[] friends) {
        Set<Integer> set = new HashSet<>();
        
        for (int i = 0; i < friends.length; i++) {
            set.add(friends[i]);
        }
        
        List<Integer> resultList = new ArrayList<>();
        
        for (int i = 0; i < order.length; i++) {
            if (set.contains(order[i])) {
                resultList.add(order[i]);
            }
        }
        
        int[] ans = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            ans[i] = resultList.get(i);
        }
        
        return ans;
    }
}
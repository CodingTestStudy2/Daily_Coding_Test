/* 

1. 아이디어 : boolean으로 최종 켜져있는 전구 확인, 총 100개 이하의 전구이므로, 미리 배열 저장

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public List<Integer> toggleLightBulbs(List<Integer> bulbs) {
        //켜져있는 전구 반환
        //최종적으로 켜져있는 전구

        boolean[] isTurnedOn = new boolean[101];

        for(int i=0; i<bulbs.size(); i++) {
            int n = bulbs.get(i);
            if(!isTurnedOn[n]) isTurnedOn[n] = true;
            else isTurnedOn[n] = false;
        }

        List<Integer> ans = new ArrayList<>();
        for(int i=0; i<101; i++) {
            if(isTurnedOn[i]) ans.add(i);
        }

        return ans;
    }
}
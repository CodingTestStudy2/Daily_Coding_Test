/*

1. 아이디어 : 10진법 숫자를 2진법 변환시 모든 숫자가 0이나 1인 수의 개수
             경우의 수가 0,1,11,111,111 .. 로 정해져 있으므로 n이하의 조건을 만족하는 수만 미리 구하면 된다

2. 시간복잡도 : O(logN)

3. 자료구조/알고리즘 : 완전탐색

 */
class Solution {
    public int countMonobit(int n) {
        // 포함되는 모든 bit가 같을때 

        //0, 1, 1+2, 1+2+4, 1+2+4+8 ..

        List<Integer> list = new ArrayList<>();
        list.add(0);

        int num = 0;
        int idx = 0;
        while(num<=n) {
            int add = (int)Math.pow(2,idx++);
            if((num+add)>n) break;
            num+=add;

            list.add(num);
        }

        return list.size();
    }
}
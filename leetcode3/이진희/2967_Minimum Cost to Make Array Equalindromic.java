/* 2차 해결
1. 아이디어 : 중앙값을 이용해 계산
            최소의 합을 만족하는 펠린드롬 숫자 K는 중앙값근처의 펠린드롬 수
            중앙값을 먼저 구하고, 그 수를 조합해 팰린드롬을 생성한다
            
            후보군
            1. 중앙값의 앞 절반을 그대로 사용하여 대칭
            2. 앞 절반에서 1을 뺀 값으로 대칭
            3. 앞 절반에서 1을 더한 값으로 대칭
            4. 자릿수가 줄어드는 경우의 최댓값
            5. 자릿수가 늘어나는 경우의 최솟값

2. 시간복잡도 : O(N log N) + O(5 * N) => O(N log N)

3. 자료구조/알고리즘 : 구현

 */

class Solution {
    public long minimumCost(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int midNum = nums[n / 2];
        
        List<Long> candidate = new ArrayList<>();
        
        String s = String.valueOf(midNum);
        int len = s.length();
        
        long half = Long.parseLong(s.substring(0,(len+1)/2));
    
        for (long h : new long[]{half, half - 1, half + 1}) {
            candidate.add(makeSingle(h, len % 2 == 0));
        }
        
        candidate.add((long) Math.pow(10, len - 1) - 1);
        candidate.add((long) Math.pow(10, len) + 1);

        long ans = Long.MAX_VALUE;

        for (long c : candidate) {
            if (c < 0) continue;
            long tmp = 0;
            for (int i = 0; i < n; i++) {
                tmp += Math.abs((long) nums[i] - c);
            }
            ans = Math.min(ans, tmp);
        }

        return ans;
    }

    private long makeSingle(long half, boolean isEven) {
        long res = half;
        long tmp = half;
        
        if (!isEven) tmp /= 10; 
        
        while (tmp > 0) {
            res = res * 10 + (tmp % 10);
            tmp /= 10;
        }
        return res;
    }
}

/* 1차 해결

1. 아이디어 : 최대 10억개 이하의 팰린드롬이 존재하므로 1 ~ 99999(절반 길이)의 숫자를 조합해 10억 이하의 모든 펠린드롬을 구한다
            이후 구한 펠린드롬을 정렬, nums 배열의 중앙값을 구해 이분탐색으로 펠린드롬배열에서 target을 찾는다
            값이 없을 경우, target 근처의 후보 target-1, target, target+1을 파악후, 가장 차이의 합이 적은 값을 구한다

2. 시간복잡도 : O(P log P) + O(N log N) + O(N)  
             P -> 최대 펠린드롬 수 범위

3. 자료구조/알고리즘 : 이진탐색 + 브루트포스

 */

// nums[i]는 최대 10억
// nums의 크기는 최대 10만
class Solution {

    static List<Integer> palindromes = new ArrayList<>();

    public long minimumCost(int[] nums) {

        long ans = Long.MAX_VALUE;
        Arrays.sort(nums);
        
        int midNum = nums[nums.length/2];

        if(palindromes.isEmpty()) makepalindrome();

        int targetIndex = Collections.binarySearch(palindromes, midNum);
        long tmp = 0L;

        if(targetIndex >= 0) {
            for(int i=0; i<nums.length; i++) {
                tmp+=Math.abs(nums[i] - palindromes.get(targetIndex));
            }
            ans = tmp;
        }
        else {
            //결과값 기준 후보
            targetIndex = -(targetIndex + 1);

            List<Integer> candidate = new ArrayList<>();
            for(int idx = targetIndex-1; idx<targetIndex+2; idx++) {
                if(idx >= palindromes.size()) continue;
                else candidate.add(palindromes.get(idx));
            }

            for(int c : candidate) {
                tmp = 0L;
                for(int j=0; j<nums.length; j++) {
                    tmp+=Math.abs(nums[j] - c);
                }
                ans = Math.min(ans, tmp);
            }
        }

        return ans;
    }

    // 미리 펠린드롬 구해놓기
    static void makepalindrome() {
        int LIMIT = 1000000000;

        for(int i=1; i<=99999; i++) {
            long even = i;
            int tmp = i;
            while (tmp>0) {
                even = even * 10 + (tmp%10);
                tmp /= 10;
            }
            if(even<LIMIT) palindromes.add((int)even);

            long odd = i;
            tmp = i/10;
            while(tmp>0) {
                odd = odd * 10 + (tmp%10);
                tmp /= 10;
            }
            if(odd<LIMIT) palindromes.add((int)odd);
        }

        // 이진 탐색을 위한 정렬
        Collections.sort(palindromes);
    }
}
/* 2차 해결

1. 아이디어 : split("[.]") 로 각 String을 분리한다
            완전탐색을 하며 각 숫자를 비교한다 (이때 삼항연산자로 불필요한 if문 간소화)

2. 시간복잡도 : O(N) (1ms)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int compareVersion(String version1, String version2) {
        String[] ver1 = version1.split("[.]");
        String[] ver2 = version2.split("[.]");

        int len = Math.max(ver1.length, ver2.length);
        for(int i=0; i<len; i++) {
            
            int v1 = (i<ver1.length) ? Integer.parseInt(ver1[i]) : 0;
            int v2 = (i<ver2.length) ? Integer.parseInt(ver2[i]) : 0;

            if(v1>v2) return 1;
            else if(v1<v2) return -1;
        }
        return 0;
    }
}

/* 1차 해결

1. 아이디어 : split("[.]") 로 각 String을 분리한다
            완전탐색을 하며 각 숫자를 비교한다

2. 시간복잡도 : O(N) (3ms)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int compareVersion(String version1, String version2) {
        String[] ver1 = version1.split("[.]");
        String[] ver2 = version2.split("[.]");

        int len = Math.max(ver1.length, ver2.length);
        for(int i=0; i<len; i++) {
            if(ver1.length>i && ver2.length>i) {
                int v1 = Integer.parseInt(ver1[i]);
                int v2 = Integer.parseInt(ver2[i]);

                if(v1>v2) return 1;
                else if(v1<v2) return -1;
            }

            else if(ver1.length<=i) {
                if(Integer.parseInt(ver2[i])>0) return -1;
            }
            else if(ver2.length<=i) {
                if(Integer.parseInt(ver1[i])>0) return 1;
            }
        }

        return 0;
    }
}
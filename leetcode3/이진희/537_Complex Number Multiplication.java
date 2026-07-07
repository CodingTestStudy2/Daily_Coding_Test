/*
1. 아이디어: 두 복소수의 곱 구하기
             문자열을 파싱하여, 직접 계산다면 된다

2. 시간복잡도: O(1)

3. 자료구조/알고리즘: 문자열, 계산

*/

class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        // 두 복소수의 곱
        //a + bi
        //c + di

        String[] n1 = num1.split("\\+");
        String[] n2 = num2.split("\\+");

        int real1 = Integer.parseInt(n1[0]);
        int imag1 = Integer.parseInt(n1[1].substring(0,n1[1].length()-1));

        int real2 = Integer.parseInt(n2[0]);
        int imag2 = Integer.parseInt(n2[1].substring(0,n2[1].length()-1));

        int multi1 = real1*real2 - imag1*imag2;
        int multi2 = real1*imag2 + real2*imag1;
        
        return multi1 + "+" + multi2 + "i";
    }
}
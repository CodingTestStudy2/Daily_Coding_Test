/*

1. 아이디어 : stack 구조 성질 활용
             push, pop을 하며 괄호가 올바르게 배치됐는지 체크

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : stack

 */

class Solution {
    public boolean isValid(String s) {
        // stack 구조 활용

        Deque<Character> stack = new ArrayDeque<>();

        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            if(c=='(' || c=='[' || c=='{') stack.add(c);
            else {
                if(stack.isEmpty()) return false;
                
                char prev = stack.pollLast();

                if(prev == '(' && c == ')') continue;
                if(prev == '{' && c == '}') continue;
                if(prev == '[' && c == ']') continue;

                return false;
            }

        }

        if(!stack.isEmpty()) return false;

        return true;
    }
}
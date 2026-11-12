/*
1. 아이디어: root부터 타고 들어가는 그리디 방식은 사전순 배열된 최소 root를 구할 수 없다
           백트랙킹으로 가지치기 해나가며 값을 구한다

2. 시간복잡도: O(Tree 높이 * 노드 수)

3. 자료구조/알고리즘: 백트랙킹

*/

class Solution {
    private String ans;
    public String smallestFromLeaf(TreeNode root) {
        // 1. 사전순, 2. 문자열 길이가 짧을 것
        // root 기준 
        StringBuilder sb = new StringBuilder();

        backtrack(root, sb);
        return ans;
    }

    private void backtrack(TreeNode node, StringBuilder sb) {
        if(node == null) return;

        sb.append((char)(node.val+'a'));

        if(node.left == null && node.right == null) {
            String tmp = sb.reverse().toString();

            if(ans == null || tmp.compareTo(ans) < 0) ans = tmp;

            sb.reverse();
        }

        backtrack(node.left, sb);
        backtrack(node.right, sb);

        sb.deleteCharAt(sb.length()-1);
    }
}
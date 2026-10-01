/*

1. 아이디어 : 이진트리에서 두 노드 사이의 가장 긴 경로 구하기
            이진트리 구조의 원리를 이용하여 dfs로 최대 간선의 길이를 구한다.

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : DFS

 */

class Solution {
    private int ans;

    public int diameterOfBinaryTree(TreeNode root) {
        ans = 0;

        dfs(root);
        return ans;
    }

    private int dfs(TreeNode node) {
        if(node == null) return 0;

        int l = dfs(node.left);
        int r = dfs(node.right);

        ans = Math.max(ans, l+r);

        return 1 + Math.max(l, r);
    }
}
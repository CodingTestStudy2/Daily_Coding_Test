/* 

1. 아이디어 : TreeNode와 DP의 성질을 활용
            후위순회로 리프 노드까지 이동 후, DP를 활용하여, 그 집을 털었을때, 털지 않았을때의 최댓값을 구해준다

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : DP(DFS)

 */
class Solution {
    public int rob(TreeNode root) {
        // 루트부터 집을 털었을때 최댓값
        // 턴집과 연결되어 있는 집은 못 텀

        int[] ans = dfs(root);

        return Math.max(ans[0], ans[1]);

    }

    private int[] dfs(TreeNode node) {
        // 기저사례 
        if(node == null) return new int[]{0,0};

        int[] left = dfs(node.left);
        int[] right = dfs(node.right);

        int[] curr = new int[2];

        // 집을 털면 받을 수 있는 최댓값
        curr[0] = node.val + left[1] + right[1];

        //집을 안털면 받을 수 있는 최댓값
        curr[1] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);

        return curr;
    }
}
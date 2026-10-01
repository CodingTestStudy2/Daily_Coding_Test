// 재귀함수
// O(n)

class Solution {
    int max;
    public int diameterOfBinaryTree(TreeNode root) {
        max = 0;
        depth(root);
        return max;
    }

    int depth(TreeNode node) {
        if (node == null) return 0;

        int left = depth(node.left);
        int right = depth(node.right);
        max = Math.max(max, left + right);

        return Math.max(left, right) + 1;
    }
}

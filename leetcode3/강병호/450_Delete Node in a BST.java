/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        // BST -> binary search tree, 순서 존재
        // return 삭제된 노드 val
        if (root == null) return null;

        if (key < root.val) {
            root.left = deleteNode(root.left, key); // 삭제 후 삭제된 노드 root left로 
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            // 삭제 할 노드 인 경우

            if (root.left == null) return root.right;
            if (root.right == null) return root.left;

            // 자식이 있는 경우 : 본인 보다 크면서 가장 최소값
            TreeNode temp = root.right;
            while (temp.left != null) {
                temp = temp.left;
            }

            root.val = temp.val;
            root.right = deleteNode(root.right, temp.val);

        }

        return root;
    }
}
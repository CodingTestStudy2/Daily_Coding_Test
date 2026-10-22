/* 

1. 아이디어 : 먼저 subTree의 노드를 rootNode에서 찾은뒤, 완전탐색으로 같은지 체크

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

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
    
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        return findPos(root, subRoot);
    }

    public boolean findPos(TreeNode root, TreeNode subRoot) {
        if(root == null) return false;

        if(checkSame(root, subRoot)) return true;

        return findPos(root.left, subRoot) || findPos(root.right, subRoot);
    }

    public boolean checkSame(TreeNode root, TreeNode subRoot) {
        if(root == null && subRoot == null) return true;
        
        if(root == null || subRoot == null || root.val != subRoot.val) return false;

        return checkSame(root.left, subRoot.left) && checkSame(root.right, subRoot.right);
    }
}
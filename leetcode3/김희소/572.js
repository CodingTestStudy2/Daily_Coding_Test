/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */

 // root 하위 트리 중에서 subRoot와 구조,노드 값 모두 같은 것 있으면 true, 아니면 false
var isSubtree = function(root, subRoot) {
    if (root === null) return false;
    if (root.val === subRoot.val) {
        
    }
};
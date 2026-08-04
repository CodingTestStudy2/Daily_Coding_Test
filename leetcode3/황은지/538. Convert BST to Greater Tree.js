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
 * @return {TreeNode}
 */
var convertBST = function (root) {
  function changeValue(preSum, root) {
    if ((root === null) | (root === undefined)) return 0;
    changeValue(0, root.right);
    const sumRight = root.right ? root.right.val : 0;
    root.val = root.val + preSum + sumRight;
    changeValue(root.val, root.left);
  }

  changeValue(0, root);
  return root;
};

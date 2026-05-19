/*

1. 아이디어 : 이진 탐색 트리의 성질을 파악해야한다
            반드시 두개의 노드는 교체되어있고, 이진트리 형태의 구조에서 root가 주어진다
            이때, 중위순위로 탐색시, 이진트리는 무조건 오름차순으로 정렬되는 특성을 가졌다
            즉, 현재 섞인 트리를 중위탐색하여, 오름차순이 아닌 부분을 체크해 교환하면 된다
            이때, 숫자가 인접하여 교체된 경우, 숫자가 떨어져 고체된 경우를 생각해야 한다

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : dfs

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
    static List<TreeNode> list;
    public void recoverTree(TreeNode root) {
        //node, left, right
        //이진 트리, 노드 기준 왼쪽은 무조건 작고, 오른쪽은 무조건 큼
        //두 노드만이 서로 뒤바뀌어 있음
        //[2,1000]

        list = new ArrayList<>();
        findTree(root);
        
        TreeNode firstNode = null;
        TreeNode secondNode = null;

        for(int i=0; i<list.size()-1; i++) {
            if(list.get(i).val<list.get(i+1).val) continue;
            if(firstNode == null) {
                firstNode = list.get(i);
                secondNode = list.get(i+1);
            }
            else secondNode = list.get(i+1);
        }

        int tmp = firstNode.val;
        firstNode.val = secondNode.val;
        secondNode.val = tmp;

    }

    static void findTree(TreeNode root) {
        if(root == null) return;

        findTree(root.left);
        list.add(root);
        findTree(root.right);
    }
}
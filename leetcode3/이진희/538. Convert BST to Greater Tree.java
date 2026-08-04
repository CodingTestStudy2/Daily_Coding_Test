/*
1. 아이디어: 특정 노드 기준으로 더 큰 노드를 전부 더해주면 된다. 
             이때 이진 탐색 트리를 중위순회 시 오름차순으로 정렬되는 원리를 사용한다.
             left -> right => 오름차순 
             right -> left => 내림차순

             지나온 값을 저장하면서 이동하면 쉽게 구할 수 있다

2. 시간복잡도: O(N)

3. 자료구조/알고리즘: 이진탐색트리 구조체 동작 원리

*/
class Solution {
    private int sum;
    public TreeNode convertBST(TreeNode root) {

        // 특정노드보다 큰 노드 전부 더하기

        if(root == null) return null;

        convertBST(root.right);
        sum+= root.val;
        root.val = sum;
        convertBST(root.left);

        return root;
    }
}
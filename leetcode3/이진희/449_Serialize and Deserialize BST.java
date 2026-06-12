/*

1. 아이디어 : 이진탐색트리구조 규칙 활용
              직렬화: 선위순회로 풀이 -> StringBuilder를 사용하여 ","로 숫자를 구분하여 저장
              역질렬화: 문자열을 "," 기준으로 파싱 후, Dqeue를 사용해 TreeNode 복원
                        이때 노드 왼쪽 자식 값 < 노드 값 < 노드 오른쪽 자식 값의 규칙이 있는걸 명심

2. 시간복잡도 : 직렬화O(N) + 역직렬화O(N) => O(N)

3. 자료구조/알고리즘 : 이진탐색트리구조, Deque

 */

public class Codec {
    // 트리구조 -> 문자열
    public String serialize(TreeNode root) {
        if(root == null) return "";

        StringBuilder sb = new StringBuilder();

        serializeHelper(root, sb);
        return sb.toString();
    }

    private void serializeHelper(TreeNode root, StringBuilder sb) {
        if(root == null) return;

        sb.append(root.val).append(",");
        serializeHelper(root.left, sb);
        serializeHelper(root.right, sb);
    }

    // 문자열 -> 트리구조
    public TreeNode deserialize(String data) {
        if(data.isEmpty()) return null;

        String[] word = data.split(",");

        Deque<Integer> dq = new ArrayDeque<>();
        for(int i=0; i<word.length; i++) {
            dq.add(Integer.parseInt(word[i]));
        }

        return deserializeHelper(dq, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private TreeNode deserializeHelper(Deque<Integer> dq, int min, int max) {
        if(dq.isEmpty()) return null;

        int val = dq.peek();
        if(val<min || val>max) return null;

        dq.poll();
        TreeNode root = new TreeNode(val);

        root.left = deserializeHelper(dq, min, val);
        root.right = deserializeHelper(dq, val, max);

        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// String tree = ser.serialize(root);
// TreeNode ans = deser.deserialize(tree);
// return ans;
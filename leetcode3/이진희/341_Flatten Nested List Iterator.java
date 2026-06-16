/*

1. 아이디어 : 주어진 인터페이스 활용, 아래 메소드를 완성
              1. public NestedIterator(List<NestedInteger> nestedList) -> nestedList 초기화
              2. public Integer next() -> 다음 수 출력
              3. public boolean hasNext() -> 현재 위치에서 nested list에 다음 Integer가 존재시 return true

              이때, 리스트 원소를 뒤부터 넣어줘야하는데, 원래 순서로 풀으려면, 나중에 들어간 요소가 먼저나와야 하기 때문

2. 시간복잡도 : 1. NestedIterator -> O(N)
                2. Integer next() -> O(1)
                3. boolean hasNext() -> O(N)

3. 자료구조/알고리즘 : Deque(Stack 처럼 활용)

 */

public class NestedIterator implements Iterator<Integer> {
    private Deque<NestedInteger> deque;

    public NestedIterator(List<NestedInteger> nestedList) {
        deque = new ArrayDeque<>();

        for(int i=nestedList.size()-1; i>=0; i--) {
            deque.push(nestedList.get(i));
        }
    }

    @Override
    public Integer next() {
        int num = deque.pop().getInteger();
        return num;
    }

    @Override
    public boolean hasNext() {
        while(!deque.isEmpty()) {
            boolean check = deque.peek().isInteger();

            if(check) return true;
            List<NestedInteger> list = deque.pop().getList();

            for(int i=list.size()-1; i>=0; i--) {
                deque.push(list.get(i));
            }
        }
        return false;
    }
}
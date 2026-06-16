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
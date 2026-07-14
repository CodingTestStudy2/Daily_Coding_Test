/*

1. 아이디어 : 요구사항대로 Deque 함수 구현

2. 시간복잡도 : O(1)

3. 자료구조/알고리즘 : Deque

 */

class MyCircularDeque {
    Deque<Integer> dq;
    int size;

    public MyCircularDeque(int k) {
        dq = new ArrayDeque<>();
        size = k;
    }
    
    public boolean insertFront(int value) {
        if(dq.size() == size) return false;
        dq.addFirst(value);
        return true;
    }
    
    public boolean insertLast(int value) {
        if(dq.size() == size) return false;
        dq.addLast(value);
        return true;
    }
    
    public boolean deleteFront() {
        if(dq.isEmpty()) return false;
        dq.removeFirst();
        return true;
    }
    
    public boolean deleteLast() {
        if(dq.isEmpty()) return false;
        dq.removeLast();
        return true;
    }
    
    public int getFront() {
        if(dq.isEmpty()) return -1;
        return dq.getFirst();   
    }
    
    public int getRear() {
        if(dq.isEmpty()) return -1;
        return dq.getLast();
    }
    
    public boolean isEmpty() {
        if(dq.isEmpty()) return true;
        return false;
    }
    
    public boolean isFull() {
        if (dq.size() == size) return true;
        return false;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */
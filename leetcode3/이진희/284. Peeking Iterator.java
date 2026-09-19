/*

1. 아이디어 : Iterator 구현체 메소드를 활용하여, peek()메소드 구현
            공식 ref를 참고, peekVal 변수를 추가하고 미리 생성자 호출에서 next()를 진행해 다음값을 저장
            이때 포인터까지 이동했으므로, next(), hasNext()모두 한 칸 앞선 포인터 기준으로 오버라이딩

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 구현

 */

// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

class PeekingIterator implements Iterator<Integer> {
    private Iterator<Integer> iter;
    private int peekVal; 

	public PeekingIterator(Iterator<Integer> iterator) {
	    this.iter = iterator;
        peekVal = iter.next();
	}
	
	public Integer peek() {
        return peekVal;
	}
	
	@Override
	public Integer next() {
        int val = peekVal;
        if(iter.hasNext()) peekVal = iter.next();
        else peekVal = -1;
	    
        return val;
	}
	
	@Override
	public boolean hasNext() {
	    if(peekVal == -1) return false;
        return true;
	}
}
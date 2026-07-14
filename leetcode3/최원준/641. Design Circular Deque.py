#

'''
1. 아이디어 :
-

2. 시간복잡도 :
    O(2000 * 1)

3. 자료구조/알고리즘 :
Deque

'''
from collections import deque
class MyCircularDeque:
    max_size = 0
    dq = Deque()

    def __init__(self, k: int):
        self.max_size = k
        self.dq = Deque()

    def insertFront(self, value: int) -> bool:
        if len(self.dq) != self.max_size:
            self.dq.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.dq) != self.max_size:
            self.dq.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.dq:
            self.dq.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if self.dq:
            self.dq.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.dq:
            return self.dq[0]
        return -1

    def getRear(self) -> int:
        if self.dq:
            return self.dq[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.dq) == 0

    def isFull(self) -> bool:
        return len(self.dq) == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

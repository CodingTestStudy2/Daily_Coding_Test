class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peek_value = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.peek_value

    def next(self):
        current = self.peek_value

        if self.iterator.hasNext():
            self.peek_value = self.iterator.next()
        else:
            self.peek_value = None

        return current

    def hasNext(self):
        return self.peek_value is not None
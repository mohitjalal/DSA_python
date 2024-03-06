from SLL import *

class Stack(SLL):

    def __init__(self):
        super().__init__()
        self.count=0
    def is_empty(self):
        return super().is_empty()

    def push(self,data):
        self.insert_at_start(data)
        self.count+=1

    def pop(self):
        if not self.is_empty():
            self.delete_first()

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            raise IndexError("stack is empty")

    def size(self):
        return self.count

    def print(self):
        super().print()


S=Stack()
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.print()
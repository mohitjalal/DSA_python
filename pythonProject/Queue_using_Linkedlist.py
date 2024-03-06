from SLL import *

class Queue(SLL):
    def __init__(self):
        self.items=[]
        super().__init__()
        self.rear=None
        self.front=None

    def is_empty(self):
        super().is_empty()

    def enqueue(self,data):
        self.items.append(self.insert_at_start(data))

    def dequeue(self):
        self.delete_last()

    def get_front(self):
        return
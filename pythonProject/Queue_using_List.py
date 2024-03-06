class Queue:
    def __init__(self):
        self.items=[]
        self.front=None
        self.rear=None

    def is_empty(self):
        return len(self.items)==0

    def enqueue(self,data):
        self.items.append(data)

    def dequque(self):
        self.items.pop(0)

    def get_rear(self):
        return self.items[-1]

    def get_front(self):
        return self.items[0]

    def size(self):
        return len(self.items)


q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(f"The elements in queue are:{q.items} and the size of the queue is:{q.size()}. The front element is:{q.get_front()} and the rear element is:{q.get_rear()}.")
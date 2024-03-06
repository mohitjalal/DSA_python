from SLL import *

class Stack():

    def __init__(self):
        self.my_list=SLL()
        self.count=0

    def is_empty(self):
        return self.my_list.is_empty()

    def push(self,data):
        self.my_list.insert_at_start(data)
        self.count+=1

    def pop(self):
        self.my_list.delete_first()
        self.count-=1

    def peek(self):
        if not self.is_empty():
            return self.my_list.head.data

    def size(self):
        return self.count

    def print(self):
        l=[]
        l.append(self.my_list.print())
        return l

s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(f"The elements in the stack are:{s.print()} and the top element is:{s.peek()} and the size is:{s.size()}")

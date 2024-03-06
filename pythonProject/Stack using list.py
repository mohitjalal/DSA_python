class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==None

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(f"The elements in stack are:{s.items} and size of the stack is :{s.size()} and the top element is:{s.peek()}")
print("The poped element is:",s.pop())
print(f"The elements in stack are:{s.items} and size of the stack is :{s.size()} and the top element is:{s.peek()}")
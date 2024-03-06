class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.start=None
        self.count=0

    def is_empty(self):
        return self.start==None

    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.count+=1

    def pop(self):
        if not self.is_empty():
            item=self.start.data
            self.start=self.start.next
            self.count-=1
            return item
        else:
            raise IndexError("The stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise IndexError("The stack is empty")

    def size(self):
        return self.count

    def __str__(self):
        temp=self.start
        result=' '
        while temp!=None:
            result=result+str(temp.data)+' '
            temp = temp.next
        return result


s2=Stack()
s2.push(10)
s2.push(20)
s2.push(30)
s2.push(40)
print(f"The elements in stack are:{s2} and the top element is {s2.peek()} and the size of the stack is{s2.size()}")
print(f"The poped element from the stack is :{s2.pop()}")
print(f"The elements in stack are:{s2} and the top element is {s2.peek()} amd the size of the stack is {s2.size()}")

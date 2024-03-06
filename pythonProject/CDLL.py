class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None

    def insert_at_start(self,data):
        n=Node(data)
        if not self.is_empty():
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
        else:
            n.next=n
            n.prev=n
        self.start=n

    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        else:
            n.next=n
            n.prev=n
            self.start=n

    def search(self,value):
        temp=self.start
        while temp.next is not self.start:
            if temp.data==value:
                return temp
            temp=temp.next
        if self.start.data==value:
            return self.start
        else:
            return None

    def insert_after(self,data,temp):
        n=Node(data)
        if temp is not None:
            n.next=temp.next
            n.prev=temp
            temp.next.prev=n
            temp.next=n

    def delete_first(self):
        self.start.prev.next=self.start.next
        self.start.next.prev=self.start.prev
        self.start=self.start.next

    def delete_last(self):
        temp=self.start
        temp.prev.prev.next=self.start
        temp.prev=temp.prev.prev
    def print_list(self):
        temp=self.start
        while temp.next is not self.start:
            print(temp.data,end=' ')
            temp=temp.next
        print(temp.data,end=' ')


my_list=CDLL()
my_list.insert_at_start(30)
my_list.insert_at_start(50)
my_list.insert_at_start(70)
my_list.insert_at_start(10)
my_list.insert_at_start(20)
my_list.insert_at_last(60)
s=my_list.search(10)
my_list.insert_after(40,s)
my_list.print_list()
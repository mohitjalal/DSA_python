class Node:
    def __init__(self,data,prev=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next


class DLL:
    def __init__(self,head=None):
        self.head=head

    def is_empty(self):
        return self.head==None

    def insert_at_start(self,data):
        n=Node(data,next=self.head)
        if not self.is_empty():
            self.head.prev=n
        self.head=n

    def insert_at_last(self,data):
        n=Node(data)
        temp=self.head
        if not self.is_empty():
            while temp.next is not None:
                temp=temp.next
        n.prev = temp
        temp.next=n
        if temp==None:
            self.head=n
        else:
            temp.next=n

    def search(self,value):
        temp=self.head
        while temp is not None:
            if temp.data==value:
                return temp
            else:
                temp=temp.next
        return None

    def insert_after(self,data,temp):
        if temp is not None:
            n=Node(data,temp,temp.next)
            if temp.next is not None:
                temp.next.prev=n
        temp.next=n

    def delete_first(self):
        if self.head is not None:
            self.head=self.head.next
            if self.head is not None:
                self.head.prev=None

    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None

    def delete_item(self,data):
        if self.head is None:
            pass
        else:
            temp=self.head
            while temp is not None:
                if temp.data==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.head=temp.next
                    break
                temp=temp.next


    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end='  ')
            temp=temp.next


l=DLL()
l.insert_at_start(40)
l.insert_at_start(80)
l.insert_at_start(60)
l.insert_at_start(10)
l.insert_at_start(20)
l.insert_at_start(30)
l.insert_at_last(50)
s=l.search(10)
l.insert_after(25,s)
l.delete_first()
l.delete_last()
l.delete_item(25)
l.print_list()

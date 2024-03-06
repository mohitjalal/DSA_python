class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class SLL:
    def __init__(self,head=None):
        self.head=head

    def is_empty(self):
        if(self.head==None):
            return True

    def insert_at_start(self,data):
        n=Node(data,self.head)
        self.head=n

    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.head=n

    def search(self,value):
        if not self.is_empty():
            temp=self.head
            while temp.next is not None:
                if(temp.data==value):
                    return temp
                else:
                    temp=temp.next
            return None

    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n

    def delete_first(self):
        temp=self.head
        self.head=temp.next

    def delete_last(self):
        p=self.head
        q=p.next
        while q.next is not None:
            p=q
            q=q.next
        p.next=None

    def delete_iten(self,data):
        temp=self.head
        while (temp.next.data!=data):
            temp=temp.next
        temp.next=temp.next.next

    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next



my_list=SLL()
my_list.insert_at_start(20)
my_list.insert_at_start(30)
my_list.insert_at_start(10)
my_list.insert_at_start(60)
my_list.insert_at_start(40)
my_list.insert_at_start(50)
my_list.insert_at_last(100)
s=my_list.search(10)
my_list.insert_after(s,80)
my_list.delete_first()
my_list.delete_last()
my_list.delete_iten(30)
my_list.print()

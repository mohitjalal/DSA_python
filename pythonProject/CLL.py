class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class CLL:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last==None

    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n

    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n

    def Search(self,value):
        temp=self.last
        if not self.is_empty():
            while temp.next.data is not value:
                temp=temp.next
            return temp.next
        return None

    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n

    def delete_start(self):
        temp=self.last.next
        self.last.next=temp.next

    def delete_last(self):
        temp=self.last.next
        while temp.next is not self.last:
            temp=temp.next
        temp.next=self.last.next
        self.last=temp

    def delete_item(self,value):
        temp=self.last.next
        if not self.is_empty():
            while temp.next.data!=value:
                temp=temp.next
            temp.next=temp.next.next


    def print_list(self):
        temp=self.last.next
        if not self.is_empty():
            while temp is not self.last:
                print(temp.data, end=' ')
                temp=temp.next
            print(temp.data)


my_list=CLL()
my_list.insert_at_start(10)
my_list.insert_at_start(90)
my_list.insert_at_start(60)
my_list.insert_at_start(30)
my_list.insert_at_start(20)
my_list.insert_at_last(40)
s=my_list.Search(30)
my_list.insert_after(s,50)
my_list.delete_start()
my_list.delete_last()
my_list.delete_item(60)
my_list.print_list()
class Node:

    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

class LinkedList:

    def __init__(self):
        self.head=None
        self.n=0

    def __len__(self):
        return self.n

    def insert_head(self,value):
        #new node object
        new_node=Node(value)
        #create connection
        new_node.next=self.head
        #reassign head
        self.head=new_node
        #increment n
        self.n=self.n+1

    def __len__(self):
        return self.n

    def __str__(self):

        curr=self.head
        result=''
        while(curr!=None):
            result=result+str(curr.value)+'->'
            curr=curr.next
        return result[:-2]

    def append(self,value):
        new_node=Node(value)
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        self.n=self.n+1

    def InsertInMiddle(self,value,given):
        new_node=Node(value)
        curr=self.head
        while(curr.next.value!=given):
            curr=curr.next
        curr.next=new_node
        self.n=self.n+1


def Create_linked_list():
    L=LinkedList()
    L.insert_head(1)
    L.insert_head(2)
    L.insert_head(3)
    L.insert_head(4)

    print(len(L))
    print(L)
    L.append(5)
    L.InsertInMiddle(6,3)
    print(len(L))
    print(L)

Create_linked_list()
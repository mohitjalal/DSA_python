class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self):
        self.start=None

    def Insertion(self,data):
        n=Node(data)
        if self.start==None:
            self.start=n
        else:
            if data<self.start.item:
                while self.start.item!=None:
                    self.start=self.start.left
                self.start.left=n
            else:
                while self.start.item!=None:
                    self.start=self.start.right
                self.start.right=n
        self.Inorder_Traversing(self.start.item)

    def Inorder_Traversing(self,value):
        print(value)
        self.Inorder_Traversing(self.start.left.item)
        self.Inorder_Traversing(self.start.right.item)


b=BST()
b.Insertion(50)
b.Insertion(30)
b.Insertion(10)
b.Insertion(40)
b.Insertion(70)
b.Insertion(60)
b.Insertion(80)

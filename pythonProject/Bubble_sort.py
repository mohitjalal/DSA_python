class Bubble:
    def __init__(self,l):
        self.l=l

    def Bubble_sort(self,n):
        for i in range(n):
            for j in range(n):
                if(self.l[j]>=self.l[j+1]):
                    temp=self.l[i]
                    self.l[i]=self.l[i+1]
                    self.l[i+1]=temp
                else:
                    pass
        return self.l


l=[6,3,5,1,2]
b=Bubble(l)
print(b.Bubble_sort(len(l)))
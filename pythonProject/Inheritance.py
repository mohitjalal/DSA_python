class Phone:

    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a phone.")

'''class Smartphone(Phone):

    """This is known as the function overriding or method overriding
     where we are making a buy method in child class and we will call
      the buy function then the smartphone buy will get print."""
      
    def buy(self):
        print("Buying a smartphone.")

s=Smartphone(50000,"Apple",13)
s.buy()

'''

class SmartPhone(Phone):

    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram

s=SmartPhone(200000,'Apple',13,"mac",16)
print(s.os)
print(s.brand)
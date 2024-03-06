class Customer:

    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def __str__(self):
        return "{} is the customer name and gender is {} and lives in {}".format(self.name,self.gender,self.address)

    def change_profile(self,new_name,city):

class Address:

    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state

    def __str__(self):
        return "{} and pincode is {} and it is in the state {}.".format(self.city,self.pincode,self.state)

add=Address("Haldwani",263126,"Uttarakhand")
c1=Customer("Mohit","Male", add)

print(c1)
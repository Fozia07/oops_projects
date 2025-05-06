#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "HBL"
    def __init__(self,account_holder):
        self.account_holder =account_holder
    

    @classmethod
    def change_name(cls,name):
        cls.bank_name=name


    def display(self):
        print(f"accont holder name : {self.account_holder} \n bank name : {Bank.bank_name}")    

#default bank name  

b1=Bank("Ali")
b1.display()

#change bank name

b1.change_name("MCB")

#display change in bank name
b1.display()
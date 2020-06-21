


class CheckingAccount:
    def __init__(self,name,balance):
       self.name=name
       self.balance=balance

    def add_amount(self,amount):
        self.balance+=amount

    def __str__(self):
        return "{} and {}".format(self.name,self.balance)

sa=CheckingAccount("shashank",100)
sa.add_amount(200)
print(sa)

class Saving_Account:
    withdraw_count=0
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def withdraw_amount(self,amount):
        if self.withdraw_count <1:
            self.balance-=amount
            self.withdraw_count+=1
        else:
            print('Cannot withdraw the amount')

    def __str__(self):
        return "{} {}".format(self.name,self.balance)

sa=Saving_Account("Shashank",300)
sa.withdraw_amount(100)
sa.withdraw_amount(20)
print(sa)
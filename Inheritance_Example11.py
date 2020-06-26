class Account:
    def __init__(self,number,client,balance):
        self.name = number
        self.client = client
        self.balance =balance

    def display_balance(self):
        print(f'The balance is {self.balance}')

class SavingsAccount(Account):
    def __init__(self,number,client,balance,interest):
        Account.__init__(self,number,client,balance)
        self.interest = interest

    def display_interst(self):
        print('The interest is {}'.format(self.interest))

sa=SavingsAccount('6434','Gino',100,0.02)
sa.display_balance()
sa.display_interst()
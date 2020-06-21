class Bank_Account:
    bank_account_created=0
    def __init__(self,name,balance,number):
        self.number=number
        self.balance=balance
        self.name=name
        self.bank_account_created+=1

    def balance_of_person(self):
        print("{} balance is".format(self.balance))

bank_account1=Bank_Account('shashank',100,12)
bank_account2=Bank_Account('Deepu',163,25)

bank_account1.balance_of_person()
bank_account2.balance_of_person()
print(bank_account2.bank_account_created)


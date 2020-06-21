class Bank:
    def __init__(self,owner,initial_deposit,number):
        self.owner = owner
        self.initial_deposit = initial_deposit
        self.number = number

    def display_data(self,show=True):
        print("========Bank Data ================")
        print("Account number {}".format(self.number))
        if show:
            print(self.owner)
        print("Amount {}".format(self.initial_deposit))

b1=Bank('deepu',3000,123)
b1.display_data()
b2=Bank('sonu',3232,1331)
b2.display_data(False)
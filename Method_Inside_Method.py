class Tax_Register:
    tax = 0.05
    def __init__(self,cashier,serial):
        self.cashier = cashier
        self.serial = serial

    def display(self,subtotal):
        print("======Initial Amount ============")
        print('subtotal'+str(subtotal))
        print("tax_amount"+str(self.calculate_total(subtotal)))


    def calculate_tax(self,subtotal):
        return subtotal*self.tax

    def calculate_total(self,subtotal):
        return subtotal+self.calculate_tax(subtotal)

tr=Tax_Register("abc","1332")
tr.display(100)
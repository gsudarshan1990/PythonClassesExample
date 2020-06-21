class House:
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        if new_price >0 and isinstance(new_price,int):
            self._price = new_price
        else:
            print('Enter the number')

h1=House(5000)
print(h1.price)
h1.price=6000
print(h1.price)
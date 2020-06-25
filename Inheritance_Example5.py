class Product:
    def __init__(self,code,price,brand):
        self.code = code
        self.price = price
        self.brand = brand

    def display_product(self):
        print("========product description ===========")
        print("code",self.code)
        print("price",self.price)
        print("brand",self.brand)

class Butter(Product):
    def __init__(self,code,price,brand,expiration_date,temp):
        Product.__init__(self,code,price,brand)
        self.expiration_date =expiration_date
        self.temp = temp

class Shampoo(Product):
    def __init__(self,code,price,brand,size):
        Product.__init__(self,code,price,brand)
        self.size =size
b=Butter(100,10,"amul",'25-6-2020',100)
b.display_product()
s=Shampoo(120,1,"clinic plus",10)
s.display_product()
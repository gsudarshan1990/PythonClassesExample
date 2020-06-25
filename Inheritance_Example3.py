class Vehicle:
    def __init__(self, speed, miles, price):
        self._speed = speed
        self._miles = miles
        self._price = price

class Truck(Vehicle):
    def __init__(self,speed,miles,price,driver):
        Vehicle.__init__(self,speed,miles,price)
        self._driver = driver

t1 = Truck(100,120,3000,"ansari")
print(t1._driver)
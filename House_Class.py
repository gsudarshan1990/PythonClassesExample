class House:
    def __init__(self, price, size, rooms, location):
        self.price=price
        self.size=size
        self.rooms=rooms
        self.location=location

h1=House(100,24,3,'london')
print(h1.price)
print(h1.location)
h1.price=300
print(h1.price)
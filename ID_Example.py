names=[1,3,5,3]
names2=[1,3,5,3]
print(id(names))
print(id(names2))

class Circle:
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color



c1=Circle(10,'blue')
print(c1)
print(id(c1))
print(hex(id(c1)))

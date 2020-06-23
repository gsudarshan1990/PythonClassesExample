a=[3,4,5,9]
b=a
print(b)
print(a)

dict1={'sonu':'A','deepu':'B','Nitin':'C'}
dict2 = dict1
print(dict2)
print(dict1)
print(id(dict1))
print(id(dict2))

class Circle:
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color

circle1 = Circle(10,'red')
my_circle = circle1
print(id(my_circle))
print(id(circle1))


a=[1,2,3,4,5,6]
b=a
a[2]=7
print(b)
print(a)
a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
print("a is b "+str(a is b))
print("a == b "+str(a == b))
c=a
print(c is a)

class Dog:
    def __init__(self,age):
        self.age = age


d1=Dog(5)
d2=Dog(5)
d3=d1
print("d1 ==d1 "+str(d1 == d2))
print("d3 == d1"+str(d3 == d1))
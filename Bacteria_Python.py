class Bacteria:
    life_counter=0
    def __init__(self,membrane_type,cellular_type,size,name,kingdom,x_co_ordinate,y_co_ordinate):
        self.membrane_type=membrane_type
        self.cellular_type=cellular_type
        self.size=size
        self.name=name
        self.kingdom=kingdom
        self.x=x_co_ordinate
        self.y=y_co_ordinate
        Bacteria.life_counter+=1
    def __str__(self):
        return "{} {} {} {} {} ".format(self.membrane_type,self.cellular_type,self.size,self.name,self.kingdom)

b1=Bacteria("m1","c1",10,"amobea","monear1",10,20)
b2=Bacteria("m2","c2",20,"lacto","monera2",30,40)
b3=Bacteria("m3","c3",30,"yeast","monera3",50,60)

print(b1)
print(b2)
print(b3)

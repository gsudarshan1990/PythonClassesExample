class Patient:
    def __init__(self,name,age,allergies=None,num_children=0):
        self.name=name
        self.age=age
        self.allergies=allergies
        self.num_children=num_children

    def __str__(self):
        return "{} {} {} {}".format(self.name,self.age,self.allergies,self.num_children)

p1=Patient('deepu',30,'lung',2)
p2=Patient('sonu',30)
p3=Patient('shiva',34,num_children=1)
print(p1)
print(p2)
print(p3)
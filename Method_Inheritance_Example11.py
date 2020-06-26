class Shape:
    def __init__(self, color, description, is_polygon):
        self.color = color
        self.description = description
        self.is_polygon = is_polygon

    def display_data(self):
        print(f'========{self.description.capitalize()}==============')
        print("Color: ",self.color)
        print("is_polygon: ","yes" if self.is_polygon else "No")

class Triangle(Shape):
    def __init__(self, color, vertices,base,height):
        Shape.__init__(self,color,"triangle",True)
        self.vertices = vertices
        self.base = base
        self.height = height

class Circle(Shape):
    def __init__(self,color,radius):
        Shape.__init__(self,color,"circle",False)
        self.radius = radius

t1=Triangle("red",[(0,0),(1,2),(3,1)],3,4)
t1.display_data()

c1=Circle("blue",5)
c1.display_data()


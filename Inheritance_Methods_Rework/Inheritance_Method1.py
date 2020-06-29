class Shape:
    def __init__(self, color, is_polygon, description):
        self.color = color
        self.is_polygon = is_polygon
        self.description = description

    def display_data(self):
        print(f'=============={self.description.capitalize()}====================')
        print("Color: ",self.color)
        print("is_polygon: ","yes" if self.is_polygon else "No")

class Triangle(Shape):
    def __init__(self, color, vertices, base, height):
        Shape.__init__(self,color,"Yes","triangle")
        self.vertices = vertices
        self.base = base
        self.height = height

class Circle(Shape):
    def __init__(self,color,radius):
        Shape.__init__(self,color,"No","circle")
        self.radius = radius

c1=Circle("blue",10)
c1.display_data()
t1=Triangle("red",[(2,0),(1,3),(1,4)],5,6)
t1.display_data()
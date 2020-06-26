class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def find_area(self):
        return ((self.base*self.height)/2)

class RightAngleTriangle(Triangle):
    def __init__(self,base,height):
        Triangle.__init__(self,base,height)

    def find_area(self):
        return Triangle.find_area(self)

rt=RightAngleTriangle(5,6)
area=rt.find_area()
print(area)

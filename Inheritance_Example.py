class Fruit:
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor

class Apple(Fruit):
    def __str__(self):
        return "{} {}".format(self.color,self.flavor)

green_apple=Apple("red","sweet")
print(green_apple)